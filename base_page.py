from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def wait_for_url(self, url_pattern: str):
        expect(self.page).to_have_url(url_pattern)
