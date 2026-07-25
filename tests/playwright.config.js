// @ts-check
const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: '.',
  timeout: 30000,
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:8080',
    screenshot: 'only-on-failure',
  },
});

// To run locally:
//   1. npm init -y && npm i -D @playwright/test && npx playwright install
//   2. serve the site root, e.g.: npx http-server .. -p 8080   (run from /tests)
//   3. npx playwright test
