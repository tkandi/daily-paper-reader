(function (root, factory) {
  const api = factory(root || {});
  if (typeof module === 'object' && module.exports) {
    module.exports = api;
  }
  if (root) {
    root.DPRLocalLLM = api;
    if (root.document && typeof root.fetch === 'function') {
      api.load().catch(function () {
        // 本地 LLM 是可选增强；未运行本地服务时保持静默。
      });
    }
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function (root) {
  let state = {
    loaded: false,
    configured: false,
    provider: '',
    baseUrl: '',
    summaryModel: '',
    models: [],
  };
  let loadingPromise = null;

  const normalizeText = (value) => String(value || '').trim();

  const isLoopbackHostname = (hostname) => {
    const host = normalizeText(hostname).toLowerCase().replace(/^\[|\]$/g, '');
    return host === 'localhost' || host === '127.0.0.1' || host === '::1';
  };

  const getLocalApiBase = () => {
    const explicit = normalizeText(root.DPR_LOCAL_API_BASE).replace(/\/+$/, '');
    if (explicit) return explicit;
    const loc = root.location || {};
    const hostname = normalizeText(loc.hostname);
    if (!isLoopbackHostname(hostname)) return '';
    const protocol = normalizeText(loc.protocol) || 'http:';
    const currentPort = normalizeText(loc.port);
    if (currentPort === '8567') {
      return `${protocol}//${hostname}${currentPort ? `:${currentPort}` : ''}`;
    }
    return `${protocol}//${hostname}:8567`;
  };

  const sanitizeModels = (values) => {
    const source = Array.isArray(values) ? values : [];
    const out = [];
    const seen = new Set();
    source.forEach((value) => {
      const model = normalizeText(value);
      const key = model.toLowerCase();
      if (!model || seen.has(key)) return;
      seen.add(key);
      out.push(model);
    });
    return out;
  };

  const buildModelEntries = (config, apiBase) => {
    const models = sanitizeModels(config && config.models);
    const proxyBase = `${apiBase}/api/local/llm`;
    const endpoint = `${proxyBase}/v1/chat/completions`;
    return models.map((name) => ({
      name,
      apiKey: 'local-proxy',
      baseUrl: proxyBase,
      endpoint,
      localProxy: true,
      provider: normalizeText(config && config.provider) || 'openai-compatible',
    }));
  };

  const emitReady = () => {
    try {
      if (!root.document || typeof root.CustomEvent !== 'function') return;
      root.document.dispatchEvent(
        new root.CustomEvent('dpr-local-llm-ready', { detail: getState() }),
      );
    } catch {
      // ignore optional event failures
    }
  };

  const load = ({ force = false } = {}) => {
    if (loadingPromise && !force) return loadingPromise;
    const apiBase = getLocalApiBase();
    if (!apiBase || typeof root.fetch !== 'function') {
      state = { ...state, loaded: true };
      return Promise.resolve(getState());
    }
    loadingPromise = root.fetch(`${apiBase}/api/local/llm/config`, { cache: 'no-store' })
      .then(async (response) => {
        if (!response || !response.ok) {
          throw new Error(`HTTP ${response ? response.status : 0}`);
        }
        const config = await response.json();
        const entries = buildModelEntries(config, apiBase);
        state = {
          loaded: true,
          configured: Boolean(config && config.configured && entries.length),
          provider: normalizeText(config && config.provider),
          baseUrl: `${apiBase}/api/local/llm`,
          summaryModel: normalizeText(config && config.summaryModel) || (entries[0] && entries[0].name) || '',
          models: entries,
        };
        emitReady();
        return getState();
      })
      .catch((error) => {
        state = { ...state, loaded: true, configured: false, models: [] };
        throw error;
      })
      .finally(() => {
        loadingPromise = null;
      });
    return loadingPromise;
  };

  const getState = () => ({
    ...state,
    models: state.models.map((item) => ({ ...item })),
  });

  const getChatModels = () => state.models.map((item) => ({ ...item }));

  const getSummaryConfig = () => {
    if (!state.configured || !state.summaryModel) return null;
    const entry = state.models.find((item) => item.name === state.summaryModel) || state.models[0];
    if (!entry) return null;
    return {
      baseUrl: entry.baseUrl,
      apiKey: entry.apiKey,
      model: entry.name,
      endpoint: entry.endpoint,
      localProxy: true,
    };
  };

  return {
    normalizeText,
    isLoopbackHostname,
    getLocalApiBase,
    sanitizeModels,
    buildModelEntries,
    load,
    getState,
    getChatModels,
    getSummaryConfig,
  };
});
