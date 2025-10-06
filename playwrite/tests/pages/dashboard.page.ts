import { BasePage } from './base.page';
import { expect } from '../fixtures/test.fixture';

export class DashboardPage extends BasePage {
  private readonly welcomeMessage = '[data-testid="welcome-message"]';
  private readonly userAvatar = '[data-testid="user-avatar"]';
  private readonly logoutButton = '[data-testid="logout-button"]';
  private readonly navigationMenu = '[data-testid="nav-menu"]';

  async expectToBeLoaded(): Promise<void> {
    await this.waitForElement(this.welcomeMessage);
    await this.waitForElement(this.userAvatar);
  }

  async getUserWelcomeMessage(): Promise<string> {
    return this.getText(this.welcomeMessage);
  }

  async logout(): Promise<void> {
    await this.clickElement(this.userAvatar);
    await this.clickElement(this.logoutButton);
  }

  async navigateToSection(section: string): Promise<void> {
    const sectionSelector = `[data-testid="nav-${section.toLowerCase()}"]`;
    await this.clickElement(sectionSelector);
  }
}