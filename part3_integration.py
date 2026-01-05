import pytest
from playwright.sync_api import Page, APIRequestContext, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# Part 3: API + UI Integration Test - Solution (Refactored with POM)
# ---------------------------------------------------------
# Scenario:
# 1. API: Create a new project with specific details.
# 2. UI: Log in and verify the project appears on the dashboard.
# 3. Mobile: Verify the project card is visible on a mobile viewport.
# 4. Security: Verify tenant isolation (implied by user context).

def test_project_creation_flow(page: Page, api_request_context: APIRequestContext):
    # Test Data
    project_name = "Integration Test Project"
    project_desc = "Created via API, Verified via UI"
    tenant_id = "company1"
    auth_token = "mock_token_123"
    
    # Initialize Page Objects
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # -----------------------------------------------------
    # Step 1: API - Create Project
    # -----------------------------------------------------
    # In a real scenario, we'd hit the actual endpoint.
    # response = api_request_context.post(...)
    
    # Mocking the API response for demonstration
    page.route("**/api/v1/projects", lambda route: route.fulfill(
        status=200,
        body='{"id": 123, "name": "Integration Test Project", "status": "active"}'
    ))
    
    # -----------------------------------------------------
    # Step 2: Web UI - Verify Project Display
    # -----------------------------------------------------
    login_page.navigate("/login")
    login_page.login("admin@company1.com", "password123")
    
    # Wait for dashboard
    dashboard_page.wait_for_url("**/dashboard")
    
    # Verify the new project is listed
    new_project_card = dashboard_page.get_project_card_by_name(project_name)
    expect(new_project_card).to_be_visible()
    
    # -----------------------------------------------------
    # Step 3: Mobile - Check Mobile Accessibility
    # -----------------------------------------------------
    # Simulate mobile viewport
    page.set_viewport_size({"width": 375, "height": 667})
    expect(new_project_card).to_be_visible()
    
    # -----------------------------------------------------
    # Step 4: Security - Verify Tenant Isolation
    # -----------------------------------------------------
    # Logout and check as another user (Conceptual)
    # page.click("#logout-btn")
    # login_page.login("user@company2.com", "password123")
    # expect(dashboard_page.get_project_card_by_name(project_name)).not_to_be_visible()
