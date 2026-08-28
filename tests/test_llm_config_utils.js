const assert = require('node:assert/strict');

const {
  normalizeBaseUrlForStorage,
  buildChatCompletionsEndpoint,
  buildModelsEndpoint,
  extractModelIds,
  sanitizeModelList,
  resolveChatModels,
  resolveSummaryLLM,
  inferProviderType,
  getDeepSeekPreset,
  getOpenAICompatiblePreset,
  inferChatApiProfile,
  resolveJsonResponseMode,
  isDeepSeekV4Model,
  resolveMaxOutputTokens,
  shouldUseXApiKeyHeader,
  buildStreamingChatPayload,
  buildConnectivityTestPayload,
} = require('../app/llm-config-utils.js');

function testNormalizeBaseUrlForStorage() {
  assert.equal(
    normalizeBaseUrlForStorage('https://api.example.com/v1/chat/completions'),
    'https://api.example.com/v1',
  );
  assert.equal(
    normalizeBaseUrlForStorage('https://api.example.com/v1/'),
    'https://api.example.com/v1',
  );
}

function testBuildChatCompletionsEndpoint() {
  assert.equal(
    buildChatCompletionsEndpoint('https://api.example.com/v1'),
    'https://api.example.com/v1/chat/completions',
  );
  assert.equal(
    buildChatCompletionsEndpoint('https://api.example.com/custom-root'),
    'https://api.example.com/custom-root/v1/chat/completions',
  );
}

function testBuildModelsEndpointAndExtractIds() {
  assert.equal(buildModelsEndpoint('http://127.0.0.1:8317'), 'http://127.0.0.1:8317/v1/models');
  assert.equal(buildModelsEndpoint('https://api.example.com/v1'), 'https://api.example.com/v1/models');
  assert.deepEqual(
    extractModelIds({ data: [{ id: 'gpt-a' }, { id: 'gpt-b' }, { id: 'gpt-a' }] }),
    ['gpt-a', 'gpt-b'],
  );
}

function testSanitizeModelList() {
  assert.deepEqual(
    sanitizeModelList(['deepseek-v4-flash', ' deepseek-v4-flash ', 'deepseek-v4-pro', 'custom-model', 'extra'], 3),
    ['deepseek-v4-flash', 'deepseek-v4-pro', 'custom-model'],
  );
}

function testResolveChatModelsAndSummary() {
  const secret = {
    summarizedLLM: {
      apiKey: 'sk-summary',
      baseUrl: 'https://api.example.com/v1',
      model: 'gpt-4.1-mini',
    },
    chatLLMs: [
      {
        apiKey: 'sk-chat',
        baseUrl: 'https://api.example.com/v1/',
        models: ['gpt-4.1-mini', 'claude-sonnet-4'],
      },
    ],
  };

  const chatModels = resolveChatModels(secret);
  assert.equal(chatModels.length, 2);
  assert.deepEqual(chatModels.map((item) => item.name), [
    'gpt-4.1-mini',
    'claude-sonnet-4',
  ]);

  const summary = resolveSummaryLLM(secret);
  assert.equal(summary.model, 'gpt-4.1-mini');
  assert.equal(summary.baseUrl, 'https://api.example.com/v1');
}

function testInferProviderType() {
  assert.equal(
    inferProviderType({
      summarizedLLM: {
        apiKey: 'sk',
        baseUrl: 'https://api.deepseek.com',
        model: 'deepseek-v4-flash',
      },
    }),
    'deepseek',
  );
  assert.equal(
    inferProviderType({
      llmProvider: { type: 'cliproxyapi' },
      summarizedLLM: {
        apiKey: 'local-key',
        baseUrl: 'http://127.0.0.1:8317',
        model: 'gpt-5.4-mini',
      },
    }),
    'cliproxyapi',
  );
  assert.equal(
    inferProviderType({
      summarizedLLM: {
        apiKey: 'sk',
        baseUrl: 'https://example.com/v1',
        model: 'other-model',
      },
    }),
    'openai-compatible',
  );
}

function testGetDeepSeekPreset() {
  assert.deepEqual(
    getDeepSeekPreset('deepseek'),
    {
      key: 'deepseek',
      label: 'DeepSeek 官方',
      baseUrl: 'https://api.deepseek.com',
      models: ['deepseek-v4-flash', 'deepseek-v4-pro'],
    },
  );
  assert.equal(getDeepSeekPreset('other-a'), null);
  assert.equal(getDeepSeekPreset('other-b'), null);
  assert.equal(getDeepSeekPreset('other-c'), null);
  assert.equal(getDeepSeekPreset('other-d'), null);
  assert.deepEqual(
    getOpenAICompatiblePreset('cliproxyapi'),
    {
      key: 'cliproxyapi',
      label: '本机 CLIProxyAPI',
      baseUrl: 'http://127.0.0.1:8317',
      models: [],
    },
  );
}

function testInferChatApiProfile() {
  assert.equal(
    inferChatApiProfile('https://api.deepseek.com', 'deepseek-v4-flash'),
    'deepseek',
  );
  assert.equal(inferChatApiProfile('https://example.com/v1', 'other-model'), 'openai-compatible');
  assert.equal(inferChatApiProfile('http://127.0.0.1:8317', 'gpt-5.4-mini'), 'cliproxyapi');
}

function testResolveJsonResponseMode() {
  assert.equal(
    resolveJsonResponseMode({
      baseUrl: 'https://api.deepseek.com',
      model: 'deepseek-v4-flash',
    }),
    'json_object',
  );
  assert.equal(
    resolveJsonResponseMode({
      baseUrl: 'https://example.com/v1',
      model: 'other-model',
      preferSchema: false,
    }),
    'json_object',
  );
}

function testResolveMaxOutputTokens() {
  assert.equal(isDeepSeekV4Model('deepseek-v4-flash'), true);
  assert.equal(isDeepSeekV4Model('deepseek-v4-pro'), true);
  assert.equal(isDeepSeekV4Model('deepseek-chat'), false);
  assert.equal(
    resolveMaxOutputTokens({
      baseUrl: 'https://api.deepseek.com',
      model: 'deepseek-v4-flash',
    }),
    393216,
  );
  assert.equal(
    resolveMaxOutputTokens({
      baseUrl: 'https://api.deepseek.com',
      model: 'deepseek-v4-pro',
    }),
    393216,
  );
  assert.equal(
    resolveMaxOutputTokens({
      baseUrl: 'https://example.com/v1',
      model: 'other-model',
    }),
    null,
  );
}

function testShouldUseXApiKeyHeader() {
  assert.equal(
    shouldUseXApiKeyHeader({
      baseUrl: 'https://example.com/v1',
      model: 'other-model',
    }),
    true,
  );
  assert.equal(
    shouldUseXApiKeyHeader({
      baseUrl: 'https://example.com/v1',
      model: 'other-model',
    }),
    true,
  );
}

function testBuildStreamingChatPayload() {
  assert.deepEqual(
    buildStreamingChatPayload({
      baseUrl: 'https://api.deepseek.com',
      model: 'deepseek-v4-flash',
      messages: [{ role: 'user', content: 'hi' }],
    }),
    {
      model: 'deepseek-v4-flash',
      messages: [{ role: 'user', content: 'hi' }],
      stream: true,
      max_tokens: 393216,
    },
  );

  assert.deepEqual(
    buildStreamingChatPayload({
      baseUrl: 'https://api.deepseek.com',
      model: 'deepseek-v4-pro',
      messages: [{ role: 'user', content: 'hi' }],
    }),
    {
      model: 'deepseek-v4-pro',
      messages: [{ role: 'user', content: 'hi' }],
      stream: true,
      max_tokens: 393216,
    },
  );

}

function testBuildConnectivityTestPayload() {
  assert.deepEqual(
    buildConnectivityTestPayload({
      baseUrl: 'https://api.deepseek.com',
      model: 'deepseek-v4-pro',
    }),
    {
      model: 'deepseek-v4-pro',
      messages: [
        { role: 'system', content: 'Reply with exactly: hello world' },
        { role: 'user', content: 'hello world' },
      ],
      stream: false,
      temperature: 0,
      max_tokens: 256,
    },
  );

  assert.deepEqual(
    buildConnectivityTestPayload({
      baseUrl: 'https://api.deepseek.com',
      model: 'deepseek-v4-flash',
    }),
    {
      model: 'deepseek-v4-flash',
      messages: [
        { role: 'system', content: 'Reply with exactly: hello world' },
        { role: 'user', content: 'hello world' },
      ],
      stream: false,
      temperature: 0,
      max_tokens: 256,
    },
  );

  assert.deepEqual(
    buildConnectivityTestPayload({
      baseUrl: 'http://127.0.0.1:8317',
      model: 'gpt-5.4-mini',
    }),
    {
      model: 'gpt-5.4-mini',
      messages: [
        { role: 'system', content: 'Reply with exactly: hello world' },
        { role: 'user', content: 'hello world' },
      ],
      stream: false,
    },
  );

}

testNormalizeBaseUrlForStorage();
testBuildChatCompletionsEndpoint();
testBuildModelsEndpointAndExtractIds();
testSanitizeModelList();
testResolveChatModelsAndSummary();
testInferProviderType();
testGetDeepSeekPreset();
testInferChatApiProfile();
testResolveJsonResponseMode();
testResolveMaxOutputTokens();
testShouldUseXApiKeyHeader();
testBuildStreamingChatPayload();
testBuildConnectivityTestPayload();

console.log('llm config utils tests passed');
