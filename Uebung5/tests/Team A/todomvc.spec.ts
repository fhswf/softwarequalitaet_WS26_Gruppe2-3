// Erstellt von JSOS & BNFT

import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://demo.playwright.dev/todomvc/#/');
  await expect(page.getByRole('heading')).toContainText('todos');
  await expect(page.getByRole('textbox', { name: 'What needs to be done?' })).toBeVisible();
});
