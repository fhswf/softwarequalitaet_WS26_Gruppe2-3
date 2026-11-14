// Erstellt von JSOS & BNFT

import { expect, Page, test } from '@playwright/test';

const TODO_URL = 'https://demo.playwright.dev/todomvc/';

async function addTodo(page: Page, text: string) {
    const newTodoInput = page.getByPlaceholder('What needs to be done?');
    await newTodoInput.fill(text);
    await newTodoInput.press('Enter');
}

test.describe('TodoMVC Tests', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });

    test.describe('1. Filter-Logik überprüfen', () => {
        test('Active, Completed und All zeigen jeweils die richtigen Todos und Count', async ({ page }: { page: Page }) => {
            await addTodo(page, 'erstes Todo');
            await addTodo(page, 'zweites Todo');
            await addTodo(page, 'drittes Todo');

            // Todo 2 als erledigt markieren
            await page.getByTestId('todo-item').nth(1).getByRole('checkbox').check();
            await expect(page.getByTestId('todo-count')).toContainText('2 items left');

            // Filter: Active
            await page.getByRole('link', { name: 'Active' }).click();
            await expect(page.getByTestId('todo-item')).toHaveCount(2);
            await expect(page.getByText('erstes Todo')).toBeVisible();
            await expect(page.getByText('drittes Todo')).toBeVisible();

            // Filter: Completed
            await page.getByRole('link', { name: 'Completed' }).click();
            await expect(page.getByTestId('todo-item')).toHaveCount(1);
            await expect(page.getByText('zweites Todo')).toBeVisible();

            // Filter: All
            await page.getByRole('link', { name: 'All' }).click();
            await expect(page.getByTestId('todo-item')).toHaveCount(3);
            await expect(page.getByTestId('todo-count')).toContainText('2 items left');
        });
    });

    test.describe('2. Todo bearbeiten und abbrechen', () => {
        test('2. Todo bearbeiten und abbrechen', async ({ page }: { page: Page }) => {
            await addTodo(page, 'mein Todo V1');
            const locator = page.getByTestId('todo-title');

            // Todo bearbeiten & mit Enter bestätigen
            await locator.dblclick();
            const editedText = 'mein Todo V2';
            await page.getByRole('textbox', { name: 'Edit' }).fill(editedText);
            await locator.press('Enter');
            await expect(locator).toHaveText(editedText);

            // Todo bearbeiten & mit Escape abbrechen
            await locator.dblclick();
            const cancelledText = 'mein Todo V3';
            await page.getByRole('textbox', { name: 'Edit' }).fill(cancelledText);
            await locator.press('Escape');
            await expect(locator).toHaveText(editedText);

        });
    });

    test.describe('3. Erledigte Todos löschen', () => {
        test('3. Erledigte Todos löschen', async ({ page }: { page: Page }) => {
            //Todos anlegen und erstes als erledigt markieren
            await addTodo(page, 'erstes Todo');
            await addTodo(page, 'zweites Todo');
            await page.getByTestId('todo-item').nth(0).getByRole('checkbox').check();

            //Clear all
            await page.getByRole('button', { name: 'Clear completed' }).click();

            //Prüfen, ob Todo gelöscht wurde und persistent ist
            await page.reload();
            await page.getByRole('link', { name: 'All' }).click();
            await expect(page.getByTestId('todo-item')).toHaveCount(1);
        });
    });
});