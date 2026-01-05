import pytest
import os
from playwright.sync_api import sync_playwright

# Default configuration
BASE_URL = "https://app.workflowpro.com"

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "base_url": BASE_URL
    }

@pytest.fixture(scope="function")
def api_request_context(playwright):
    request_context = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers={
            "Content-Type": "application/json",
        }
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def authenticated_user_data():
    """
    Returns test user credentials. 
    In a real scenario, fetch these from a secure vault or .env
    """
    return {
        "email": "admin@company1.com",
        "password": "password123",
        "tenant_id": "company1"
    }
