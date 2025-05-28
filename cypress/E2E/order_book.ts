describe('Trading App - Put Order Functionality', () => {
  beforeEach(() => {
    cy.visit('https://your-app-url.com/login');
    cy.get('#username').type('user1');
    cy.get('#password').type('pass1');
    cy.get('#login').click();
    cy.contains('Dashboard').should('be.visible');
  });

  it('places a put order successfully', () => {
    cy.visit('https://your-app-url.com/trade');
    cy.get('#order-type').select('Put');
    cy.get('#stock-symbol').type('AAPL');
    cy.get('#quantity').type('10');
    cy.get('#price').type('150');
    cy.get('#place-order').click();
    cy.contains('Order placed successfully').should('be.visible');
  });

  it('shows error for invalid put order', () => {
    cy.visit('https://your-app-url.com/trade');
    cy.get('#order-type').select('Put');
    cy.get('#stock-symbol').type('INVALID');
    cy.get('#quantity').type('0');
    cy.get('#price').type('0');
    cy.get('#place-order').click();
    cy.contains('Invalid order details').should('be.visible');
  });

  it('executes a pending order successfully', () => {
    cy.visit('https://your-app-url.com/orders');
    cy.get('.order-row').contains('Pending').first().parent().within(() => {
      cy.get('.execute-order').click();
    });
    cy.contains('Order executed successfully').should('be.visible');
  });

  it('checks that a failed order appears in the order book', () => {
    cy.visit('https://your-app-url.com/orders');
    cy.get('.order-row').contains('Failed').should('exist');
  });
});
