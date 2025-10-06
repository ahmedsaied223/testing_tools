import { faker } from '@faker-js/faker';

export class TestDataGenerator {
  static generateUser() {
    return {
      firstName: faker.person.firstName(),
      lastName: faker.person.lastName(),
      email: faker.internet.email(),
      password: faker.internet.password({ length: 12 }),
      phone: faker.phone.number(),
    };
  }

  static generateProduct() {
    return {
      name: faker.commerce.productName(),
      description: faker.commerce.productDescription(),
      price: faker.commerce.price(),
      category: faker.commerce.department(),
    };
  }
}

export const waitForApiResponse = async (page: any, urlPattern: string, timeout = 10000) => {
  await page.waitForResponse(
    response => response.url().includes(urlPattern) && response.status() === 200,
    { timeout }
  );
};