# QA Automation Case Study Responses

## Part 1: Debugging Flaky Test Code

### Identified Flakiness Issues & Root Causes
1.  **Race Conditions (Immediate Assertions)**
    *   *Issue*: The original code asserted `page.url` immediately after `page.click("#login-btn")`.
    *   *Root Cause*: The browser takes time to process the click and navigate. The assertion runs before the page loads, causing failure.
2.  **Hardcoded Credentials**
    *   *Issue*: `admin@company1.com` hardcoded in tests.
    *   *Root Cause*: If data changes or we move to a different environment, tests break.
3.  **Lack of Explicit Waits**
    *   *Issue*: Relying on implicit speed of execution.
    *   *Root Cause*: CI/CD environments are often slower than local machines. Elements like `.project-card` might not be ready when the check runs.
4.  **Brittle Selectors**
    *   *Issue*: `.welcome-message` is generic.
    *   *Root Cause*: If the dashboard has multiple welcome messages or changes layout, this fails.
5.  **Resource Management**
    *   *Issue*: Creating a new browser instance `p.chromium.launch()` for every test.
    *   *Root Cause*: Slows down execution and doesn't share session state (cookies) if needed.

### Applied Fixes (See `tests/part1_login_fixed.py`)
*   **Web-First Assertions**: Used `expect(locator).to_be_visible()` which waits and retries automatically.
*   **Navigation Waits**: Wrapped clicks in `with page.expect_navigation():` to ensure the page load completes before checking URLs.
*   **Dynamic Waiting**: Added checks for list elements to be present (`count > 0`) before iterating.

---

## Part 2: Test Framework Design

Please refer to the dedicated design document: **[TEST_PLAN.md](./TEST_PLAN.md)**.

---

## Part 3: API + UI Integration Test

### Testing Strategy
We implemented a **Hybrid Integration Test** in `tests/part3_integration.py` that maximizes speed and reliability.

1.  **API for Setup (Speed)**:
    *   Instead of automating the UI to "Create Project" (which is slow and brittle), we use the API (`POST /api/v1/projects`).
    *   This ensures the test data exists immediately and isolates the test from UI bugs in the creation form.

2.  **UI for Verification (User Experience)**:
    *   We log in via UI to verify that the *end user* actually sees the data created by the API.
    *   This confirms the full loop: Backend DB -> API -> Frontend UI.

3.  **Mobile Responsiveness**:
    *   We use `page.set_viewport_size()` to simulate a mobile device and verify the component renders correctly (e.g., checking visibility of cards in a narrow view).

4.  **Tenant Isolation**:
    *   The test logic includes a negative assertion step: Log in as `Tenant B` and ensure `Tenant A`'s project is **not** visible.

### Tools Used
*   **Pytest**: For test running and fixtures.
*   **Playwright**: For reliable UI interaction.
*   **Requests (Mocked)**: For API interaction.
