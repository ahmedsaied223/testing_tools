import { test, expect } from '../fixtures/test.fixture';

test.describe('Dashboard Functionality', () => {
  test.beforeEach(async ({ loginPage, testData }) => {
    await loginPage.navigate();
    await loginPage.login(testData.validUser.email, testData.validUser.password);
  });

  test('should display user information correctly', async ({ dashboardPage }) => {
    // Assert
    await dashboardPage.expectToBeLoaded();
    const welcomeMessage = await dashboardPage.getUserWelcomeMessage();
    expect(welcomeMessage).toBeTruthy();
  });

  test('should navigate to different sections', async ({ dashboardPage, page }) => {
    // Act & Assert
    await dashboardPage.navigateToSection('profile');
    await expect(page).toHaveURL(/profile/);

    await dashboardPage.navigateToSection('settings');
    await expect(page).toHaveURL(/settings/);
  });

  test('should logout successfully', async ({ dashboardPage, page }) => {
    // Act
    await dashboardPage.logout();
    
    // Assert
    await expect(page).toHaveURL(/login/);
  });
});