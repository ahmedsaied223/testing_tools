import { Page } from '@playwright/test';

export class TestHelpers {
  static async clearLocalStorage(page: Page): Promise<void> {
    await page.evaluate(() => localStorage.clear());
  }

  static async setSessionStorage(page: Page, key: string, value: string): Promise<void> {
    await page.evaluate(([k, v]) => sessionStorage.setItem(k, v), [key, value]);
  }

  static async waitForAnimation(page: Page, selector: string): Promise<void> {
    await page.waitForFunction(
      (sel: string) => {
        const element = document.querySelector(sel);
        if (!element) return true;
        const style = window.getComputedStyle(element);
        return style.animationName === 'none' || style.animationPlayState === 'paused';
      },
      selector,
      { timeout: 5000 }
    );
  }

  static async retryOperation(
    operation: () => Promise<boolean>,
    maxAttempts = 3,
    delay = 1000
  ): Promise<boolean> {
    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
      try {
        const result = await operation();
        if (result) return true;
      } catch (error) {
        if (attempt === maxAttempts) throw error;
      }
      await new Promise(resolve => setTimeout(resolve, delay));
    }
    return false;
  }
}