import { test, expect } from '../fixtures/test.fixture';

test.describe('Login Functionality', () => {
  test('should login successfully with valid credentials', async ({ 
    loginPage, 
    dashboardPage, 
    testData 
  }) => {
    // Arrange
    await loginPage.navigate();
    
    // Act
    await loginPage.login(testData.validUser.email, testData.validUser.password);
    
    // Assert
    await dashboardPage.expectToBeLoaded();
    const welcomeMessage = await dashboardPage.getUserWelcomeMessage();
    expect(welcomeMessage).toContain('Welcome');
  });

  test('should show error message with invalid credentials', async ({ 
    loginPage, 
    testData 
  }) => {
    // Arrange
    await loginPage.navigate();
    
    // Act
    await loginPage.login(testData.invalidUser.email, testData.invalidUser.password);
    
    // Assert
    await loginPage.expectErrorMessage('Invalid credentials');
  });

  test('should redirect to forgot password page', async ({ loginPage }) => {
    // Arrange
    await loginPage.navigate();
    
    // Act
    await loginPage.clickForgotPassword();
    
    // Assert
    await expect(loginPage.page).toHaveURL(/forgot-password/);
  });

  test('should persist login session', async ({ 
    loginPage, 
    dashboardPage, 
    testData,
    page 
  }) => {
    // Login first time
    await loginPage.navigate();
    await loginPage.login(testData.validUser.email, testData.validUser.password);
    await dashboardPage.expectToBeLoaded();

    // Reload page and verify still logged in
    await page.reload();
    await dashboardPage.expectToBeLoaded();
  });
});