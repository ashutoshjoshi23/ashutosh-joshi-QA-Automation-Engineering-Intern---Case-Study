from .base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.welcome_message = page.locator(".welcome-message")
        self.project_cards = page.locator(".project-card")

    def get_project_card_by_name(self, name: str):
        return self.project_cards.filter(has_text=name)
