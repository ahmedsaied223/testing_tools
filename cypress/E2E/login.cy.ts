describe('Trading App - Login Functionality', () => {
  it('logs in with valid credentials', () => {
    cy.visit('https://your-app-url.com/login');
    cy.get('#username').type('user1');
    cy.get('#password').type('pass1');
    cy.get('#login').click();
    cy.contains('Welcome').should('be.visible');
  });

  it('shows error with invalid credentials', () => {
    cy.visit('https://your-app-url.com/login');
    cy.get('#username').type('user2');
    cy.get('#password').type('wrong');
    cy.get('#login').click();
    cy.contains('Invalid credentials').should('be.visible');
  });
});
