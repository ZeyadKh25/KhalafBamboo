// Basic smoke tests — run with: npx playwright test
// Install first: npm init -y && npm i -D @playwright/test && npx playwright install
const { test, expect } = require('@playwright/test');

const BASE = process.env.BASE_URL || 'http://localhost:8080';

test('homepage loads and has exactly one h1', async ({ page }) => {
  await page.goto(`${BASE}/index.html`);
  await expect(page).toHaveTitle(/خلف للخيزران/);
  await expect(page.locator('h1')).toHaveCount(1);
});

test('clicking a service card leads to a real category page', async ({ page }) => {
  await page.goto(`${BASE}/index.html`);
  await page.click('#services .svc-link >> nth=0');
  await expect(page).toHaveURL(/category\/.*\.html/);
  await expect(page.locator('h1')).toHaveCount(1);
});

test('clicking a product leads to a real product detail page with specs', async ({ page }) => {
  await page.goto(`${BASE}/category/outdoor.html`);
  await page.click('.prod-card >> nth=0 >> .prod-btn');
  await expect(page).toHaveURL(/product\/.*\.html/);
  await expect(page.locator('.pd-specs .pd-spec-row')).toHaveCount(5);
});

test('project filter shows/hides cards without navigating away', async ({ page }) => {
  await page.goto(`${BASE}/index.html`);
  await page.click('.filter-btn[data-f="برجولات"]');
  const visibleCards = page.locator('#projGrid .proj-card:visible');
  await expect(visibleCards).toHaveCount(1);
});

test('contact form has required fields and a real POST action', async ({ page }) => {
  await page.goto(`${BASE}/index.html#contact`);
  const form = page.locator('#quoteForm');
  await expect(form).toHaveAttribute('action', /formsubmit\.co/);
  await expect(page.locator('#f-name')).toHaveAttribute('required', '');
});

test('mobile menu opens, traps to Escape, and returns focus', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(`${BASE}/index.html`);
  await page.click('#burgerBtn');
  await expect(page.locator('#mobileMenu')).toHaveClass(/open/);
  await page.keyboard.press('Escape');
  await expect(page.locator('#mobileMenu')).not.toHaveClass(/open/);
});

test('lightbox opens with aria-modal and closes on Escape', async ({ page }) => {
  await page.goto(`${BASE}/index.html#videos`);
  await page.click('.vid-card >> nth=0');
  await expect(page.locator('#lightbox')).toHaveAttribute('aria-modal', 'true');
  await page.keyboard.press('Escape');
  await expect(page.locator('#lightbox')).not.toHaveClass(/open/);
});
