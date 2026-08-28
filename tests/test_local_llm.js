const assert = require('node:assert/strict');

const {
  isLoopbackHostname,
  sanitizeModels,
  buildModelEntries,
} = require('../app/local-llm.js');

assert.equal(isLoopbackHostname('127.0.0.1'), true);
assert.equal(isLoopbackHostname('localhost'), true);
assert.equal(isLoopbackHostname('example.github.io'), false);

assert.deepEqual(
  sanitizeModels(['gpt-a', ' gpt-a ', 'gpt-b', '']),
  ['gpt-a', 'gpt-b'],
);

assert.deepEqual(
  buildModelEntries(
    { provider: 'cliproxyapi', models: ['gpt-5.4-mini'] },
    'http://127.0.0.1:8567',
  ),
  [
    {
      name: 'gpt-5.4-mini',
      apiKey: 'local-proxy',
      baseUrl: 'http://127.0.0.1:8567/api/local/llm',
      endpoint: 'http://127.0.0.1:8567/api/local/llm/v1/chat/completions',
      localProxy: true,
      provider: 'cliproxyapi',
    },
  ],
);

console.log('local LLM tests passed');
