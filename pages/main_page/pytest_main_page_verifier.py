from playwright.sync_api import expect

from pages.main_page.pytest_main_page import PytestMainPage


class PytestMainPageVerifier:
    def __init__(self, parent_page: PytestMainPage):
        self.parent_page = parent_page

    def verifyTitle(self, title: str):
        expect(self.parent_page.title).to_contain_text(title)
        return self

    def verifyLogoIsVisible(self):
        expect(self.parent_page.logo).to_be_visible()
        return self
