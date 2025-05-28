// Custom command to log in
Cypress.Commands.add('login', (username: string, password: string) => {
  cy.visit('https://your-app-url.com/login');
  cy.get('#username').type(username);
  cy.get('#password').type(password);
  cy.get('#login').click();
  cy.contains('Dashboard').should('be.visible');
});

// Custom command to place a put order
Cypress.Commands.add('placePutOrder', (symbol: string, quantity: number, price: number) => {
  cy.visit('https://your-app-url.com/trade');
  cy.get('#order-type').select('Put');
  cy.get('#stock-symbol').type(symbol);
  cy.get('#quantity').type(quantity.toString());
  cy.get('#price').type(price.toString());
  cy.get('#place-order').click();
});

// Custom command to execute the first pending order
Cypress.Commands.add('executeFirstPendingOrder', () => {
  cy.visit('https://your-app-url.com/orders');
  cy.get('.order-row').contains('Pending').first().parent().within(() => {
    cy.get('.execute-order').click();
  });
});

// Custom command to check for a failed order in the order book
Cypress.Commands.add('checkFailedOrderInOrderBook', () => {
  cy.visit('https://your-app-url.com/orders');
  cy.get('.order-row').contains('Failed').should('exist');
});

// Custom command to check API connectivity
Cypress.Commands.add('checkApiConnectivity', () => {
  cy.request('GET', 'https://your-app-url.com/api/health')
    .its('status')
    .should('eq', 200);
});

// TypeScript declarations for custom commands
declare global {
  namespace Cypress {
    interface Chainable {
      login(username: string, password: string): Chainable<void>;
      placePutOrder(symbol: string, quantity: number, price: number): Chainable<void>;
      executeFirstPendingOrder(): Chainable<void>;
      checkFailedOrderInOrderBook(): Chainable<void>;
      checkApiConnectivity(): Chainable<void>;
    }
  }
}
export {};
