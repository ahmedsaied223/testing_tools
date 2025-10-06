import { APIRequestContext } from '@playwright/test';

export class ApiClient {
  constructor(private request: APIRequestContext) {}

  async login(credentials: { email: string; password: string }) {
    const response = await this.request.post('/api/login', {
      data: credentials,
    });
    return response;
  }

  async getUserProfile(token: string) {
    const response = await this.request.get('/api/user/profile', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response;
  }

  async createTestData(payload: any) {
    const response = await this.request.post('/api/test-data', {
      data: payload,
    });
    return response;
  }
}