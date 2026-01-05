# QA Automation Case Study - WorkFlow Pro

This repository contains the solution for the QA Automation Engineering Intern Case Study. It includes fixed test scripts, a proposed test framework design, and a comprehensive integration test scenario.

**Author**: Candidate: Ashutosh Joshi (QA Automation Engineering Intern Applicant)

## 📂 Repository Structure

```
.
├── config/                 # Configuration files (environments, capabilities)
├── pages/                  # Page Object Models (POM)
├── tests/
│   ├── part1_login_fixed.py    # Solution for Part 1 (Fixed Flaky Tests)
│   └── part3_integration.py    # Solution for Part 3 (API + UI Integration)
├── utils/                  # Utility helpers (API wrappers, data generators)
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
├── TEST_PLAN.md            # Part 2: Framework Design & Strategy (Detailed Response)
└── README.md               # This file
```

## 🚀 Setup Instructions

1.  **Clone the repository**
    ```bash
https://github.com/ashutoshjoshi23/ashutosh-joshi-QA-Automation-Engineering-Intern---Case-Study.git
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Playwright Browsers**
    ```bash
    playwright install
    ```

4.  **Run Tests**
    *   Run the fixed login tests (Part 1):
        ```bash
        pytest tests/part1_login_fixed.py
        ```
    *   Run the integration test (Part 3):
        ```bash
        pytest tests/part3_integration.py
        ```

## 🧪 Case Study Responses

### Part 1: Debugging Flaky Test Code
The corrected code is located in `tests/part1_login_fixed.py`.
*   **Key Fixes**: Replaced immediate assertions with `expect()` for auto-retrying, added proper waiting strategies, and modularized the setup using Pytest fixtures.

### Part 2: Test Framework Design
The detailed framework design document is available in [TEST_PLAN.md](./TEST_PLAN.md).
*   **Highlights**: Hybrid framework using Page Object Model (POM), Pytest fixtures for state management, and BrowserStack integration strategy.

### Part 3: API + UI Integration Test
The implementation is in `tests/part3_integration.py`.
*   **Scenario**: Creates a project via API, verifies it on the Web UI, and simulates Mobile validation.

## 🛠️ Tech Stack
*   **Language**: Python
*   **Framework**: Pytest
*   **Web Automation**: Playwright
*   **Cross-Browser/Mobile**: BrowserStack (Integration designed)
