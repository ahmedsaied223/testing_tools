# Trading App Cypress Test Framework

This project provides an automated end-to-end testing framework for the Trading App using [Cypress](https://www.cypress.io/) with TypeScript. The tests cover core trading functionalities such as login, placing put orders, executing orders, checking failed orders, and verifying API connectivity.

---

## 📦 Project Structure

```
trading-app-cypress/
├── cypress/
│   ├── e2e/
│   │   └── putorder.cy.ts
│   ├── support/
│   │   └── commands.ts
│   └── fixtures/
├── tsconfig.json
├── package.json
└── README.md
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
npm install
```

### 2. Open Cypress Test Runner

```bash
npx cypress open
```

Or run tests in headless mode:

```bash
npx cypress run
```

---

## 🧪 Test Cases

- **Login Functionality:**  
  Validates login with correct and incorrect credentials.

- **Put Order:**  
  Places a valid put order and checks for success.  
  Attempts to place an invalid order and checks for error messages.

- **Order Execution:**  
  Executes the first pending order and verifies successful execution.

- **Failed Order Check:**  
  Confirms that failed orders appear in the order book.

- **API Connectivity:**  
  Checks the health of the backend API before running tests.

---

## 🛠️ Custom Commands

Reusable commands are defined in `cypress/support/commands.ts`:
- `cy.login(username, password)`
- `cy.placePutOrder(symbol, quantity, price)`
- `cy.executeFirstPendingOrder()`
- `cy.checkFailedOrderInOrderBook()`
- `cy.checkApiConnectivity()`

---

## 📝 Usage Example

```typescript
cy.login('user1', 'pass1');
cy.placePutOrder('AAPL', 10, 150);
cy.executeFirstPendingOrder();
cy.checkFailedOrderInOrderBook();
cy.checkApiConnectivity();
```

---

## ⚙️ Configuration

- Update URLs and selectors in the test files and custom commands to match your Trading App.
- Add more test cases in `cypress/e2e/` as needed.

---

## 📚 References

- [Cypress Documentation](https://docs.cypress.io/)
- [TypeScript Support](https://docs.cypress.io/guides/tooling/typescript-support)

---

## 🏁 License

MIT
