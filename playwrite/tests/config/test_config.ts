export const TestConfig = {
  baseURL: process.env.BASE_URL || 'https://your-app.com',
  timeout: {
    navigation: 30000,
    action: 10000,
    assertion: 10000,
  },
  users: {
    admin: {
      email: process.env.ADMIN_EMAIL || 'admin@example.com',
      password: process.env.ADMIN_PASSWORD || 'admin123',
    },
    standard: {
      email: process.env.USER_EMAIL || 'user@example.com',
      password: process.env.USER_PASSWORD || 'user123',
    },
  },
  environment: process.env.NODE_ENV || 'development',
};