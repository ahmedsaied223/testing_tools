import { BasePage } from './base.page';
import { expect } from '../fixtures/test.fixture';

export class LoginPage extends BasePage {
  // Selectors
  private readonly emailInput = '[data-testid="email-input"]';
  private readonly passwordInput = '[data-testid="password-input"]';
  private readonly loginButton = '[data-testid="login-button"]';
  private readonly errorMessage = '[data-testid="error-message"]';
  private readonly forgotPasswordLink = '[data-testid="forgot-password"]';

  async navigate(): Promise<void> {
    await this.navigateTo('/login');
    await this.waitForLoad();
  }

  async login(email: string, password: string): Promise<void> {
    await this.fillField(this.emailInput, email);
    await this.fillField(this.passwordInput, password);
    await this.clickElement(this.loginButton);
  }

  async expectErrorMessage(message: string): Promise<void> {
    await this.waitForElement(this.errorMessage);
    const errorText = await this.getText(this.errorMessage);
    expect(errorText).toContain(message);
  }

  async clickForgotPassword(): Promise<void> {
    await this.clickElement(this.forgotPasswordLink);
  }

  async isLoginFormVisible(): Promise<boolean> {
    try {
      await this.waitForElement(this.emailInput, 2000);
      return true;
    } catch {
      return false;
    }
  }
}