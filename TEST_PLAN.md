# Part 2: Test Framework Design & Strategy

## 1. Framework Architecture
We will use a **Hybrid Framework** combining **Page Object Model (POM)** for UI maintainability and **Pytest** for test execution and reporting.

### Folder Structure
```
/
├── .github/workflows/      # CI/CD pipelines (GitHub Actions)
├── config/
│   ├── browserstack.json   # BrowserStack capabilities
│   └── env_config.py       # Environment-specific URLs (Dev, Staging, Prod)
├── data/
│   ├── test_data.json      # Static test data
│   └── users.json          # User roles and credentials
├── pages/                  # Page Object Models
│   ├── base_page.py        # Common methods (click, type, wait)
│   ├── login_page.py       # Login page locators and methods
│   └── dashboard_page.py   # Dashboard interactions
├── tests/
│   ├── api/                # API specific tests
│   ├── ui/                 # UI specific tests
│   └── e2e/                # End-to-end integration tests
├── utils/
│   ├── api_client.py       # Wrapper for API requests
│   ├── db_client.py        # Database helpers (for cleanup/setup)
│   └── logger.py           # Custom logging setup
├── conftest.py             # Pytest fixtures (setup/teardown, browser init)
├── pytest.ini              # Pytest configuration (markers, options)
└── requirements.txt        # Dependencies
```

## 2. Configuration Management

### Handling Multiple Environments
We will use a `config/env_config.py` or `.env` files to manage environment URLs.
*   **Usage**: Pass a command-line argument `--env=staging` to Pytest.
*   **Implementation**: The `conftest.py` fixture reads this argument and loads the appropriate base URL.

### Cross-Browser & Mobile (BrowserStack)
We will define a `driver` fixture in `conftest.py` that can switch between local Playwright browsers and a remote BrowserStack connection based on a `--remote` flag.
*   **Local**: `browser = p.chromium.launch()`
*   **Remote**: `browser = p.chromium.connect(ws_endpoint=f"wss://cdp.browserstack.com/playwright?caps={caps}")`

## 3. Key Design Decisions

### Flakiness Prevention
*   **Auto-waiting**: Rely strictly on Playwright's built-in auto-waiting (e.g., `click`, `fill`).
*   **Web-First Assertions**: Use `expect(locator).to_be_visible()` instead of `assert locator.is_visible()`. The former retries automatically.
*   **Dynamic Waits**: Avoid `time.sleep()`. Use `page.wait_for_selector()` or `page.wait_for_response()` for network states.

### Test Data Management
*   **Hybrid Approach**:
    *   **Static Data**: For standard roles (Admin, User) stored in JSON/YAML.
    *   **Dynamic Data**: Use `Faker` library to generate unique project names/emails to avoid collision in multi-tenant environments.
    *   **Cleanup**: Use API calls in the `yield` phase of fixtures to delete created data after tests.

## 4. CI/CD Integration
*   **Pipeline**: GitHub Actions or Jenkins.
*   **Triggers**: On Pull Request and Nightly.
*   **Parallelism**: Use `pytest-xdist` (`pytest -n 4`) to run tests in parallel.
*   **Reporting**: Generate Allure reports (`--alluredir=results`) for detailed visualization of pass/fail rates and screenshots.

## 5. Missing Requirements / Clarifications
To fully robustify this framework, I would ask:
1.  **Test Data Reset**: Is there a "nuke" API to reset a tenant's data to a clean state?
2.  **2FA Handling**: Is there a bypass for 2FA in test environments, or do we need to automate TOTP generation?
3.  **Mobile Scope**: Are we testing native apps (Appium needed) or just mobile web (Playwright/BrowserStack is sufficient)?
4.  **Rate Limiting**: Are there API rate limits we need to respect during parallel execution?
