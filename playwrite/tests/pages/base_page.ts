import { Page, Locator } from '@playwright/test';

export abstract class BasePage {
  constructor(protected page: Page) {}

  protected async navigateTo(url: string): Promise<void> {
    await this.page.goto(url);
  }

  protected async waitForLoad(state: 'load' | 'domcontentloaded' | 'networkidle' = 'load'): Promise<void> {
    await this.page.waitForLoadState(state);
  }

  protected async getElement(selector: string): Promise<Locator> {
    return this.page.locator(selector);
  }

  protected async clickElement(selector: string): Promise<void> {
    await this.page.click(selector);
  }

  protected async fillField(selector: string, value: string): Promise<void> {
    await this.page.fill(selector, value);
  }

  protected async getText(selector: string): Promise<string> {
    return this.page.textContent(selector) || '';
  }

  protected async waitForElement(selector: string, timeout = 5000): Promise<void> {
    await this.page.waitForSelector(selector, { timeout });
  }

  protected async takeScreenshot(name: string): Promise<Buffer> {
    return this.page.screenshot({ 
      path: `test-results/screenshots/${name}-${Date.now()}.png`,
      fullPage: true 
    });
  }
}