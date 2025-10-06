import { test as baseTest } from '@playwright/test';
import { LoginPage } from '../pages/login.page';
import { DashboardPage } from '../pages/dashboard.page';
import { ApiClient } from './api.fixture';

export interface TestFixtures {
  loginPage: LoginPage;
  dashboardPage: DashboardPage;
  apiClient: ApiClient;
  testData: any;
}

export const test = baseTest.extend<TestFixtures>({
  loginPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await use(loginPage);
  },

  dashboardPage: async ({ page }, use) => {
    const dashboardPage = new DashboardPage(page);
    await use(dashboardPage);
  },

  apiClient: async ({ request }, use) => {
    const apiClient = new ApiClient(request);
    await use(apiClient);
  },

  testData: async ({}, use) => {
    const testData = {
      validUser: {
        email: 'test@example.com',
        password: 'securepassword123'
      },
      invalidUser: {
        email: 'invalid@example.com',
        password: 'wrongpassword'
      }
    };
    await use(testData);
  },
});

export { expect } from '@playwright/test';