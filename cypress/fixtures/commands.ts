Cypress.Commands.add('login', (username: string, password: string) => {
  cy.get('#username').type(username);
  cy.get('#password').type(password);
  cy.get('#login').click();
});
