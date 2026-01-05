import os
import time
from playwright.sync_api import sync_playwright

def run_demo_and_capture():
    # Get absolute paths to mock files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    login_path = f"file://{os.path.join(base_dir, 'mock_site', 'login.html')}"
    dashboard_path = f"file://{os.path.join(base_dir, 'mock_site', 'dashboard.html')}"
    
    screenshot_dir = os.path.join(base_dir, "screenshots")
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    print("Starting Playwright Demo...")
    with sync_playwright() as p:
        # Launch browser in headed mode so the user can "see" it (if they were watching locally)
        # and to capture screenshots.
        browser = p.chromium.launch(headless=True, slow_mo=1000)
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        
        # 1. Login Page
        print(f"Navigating to Login Page: {login_path}")
        page.goto(login_path)
        page.wait_for_selector("#login-btn")
        
        # Type credentials
        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        
        # Take Screenshot 1: Login Filled
        page.screenshot(path=os.path.join(screenshot_dir, "1_login_page.png"))
        print("Captured: 1_login_page.png")
        
        # Click Login (Mock navigation)
        # Since it's a file:// navigation in the HTML onclick, we wait for load
        page.click("#login-btn")
        page.wait_for_load_state("networkidle")
        
        # 2. Dashboard Page
        print("Navigating to Dashboard...")
        # Ensure we are on dashboard
        page.wait_for_selector(".welcome-message")
        
        # Take Screenshot 2: Dashboard
        page.screenshot(path=os.path.join(screenshot_dir, "2_dashboard_desktop.png"))
        print("Captured: 2_dashboard_desktop.png")
        
        # 3. Mobile View
        print("Switching to Mobile View...")
        page.set_viewport_size({"width": 375, "height": 667})
        page.wait_for_timeout(500) # Wait for resize
        
        # Take Screenshot 3: Mobile Dashboard
        page.screenshot(path=os.path.join(screenshot_dir, "3_dashboard_mobile.png"))
        print("Captured: 3_dashboard_mobile.png")
        
        browser.close()
        print("Demo Complete! Screenshots saved in 'screenshots/' folder.")

if __name__ == "__main__":
    run_demo_and_capture()
