from playwright.sync_api import Page

from pages.get_started_page.get_started_page import GetStartedPage
from pages.BasePage import BasePage


class PytestMainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("//h1")
        self.logo = page.locator("//img[@class='sidebar-logo']")
        self.side_bar_root = page.locator("//aside[@class='sidebar-drawer']")
        self.get_started_btn = self.side_bar_root.locator("//li[.//a[text()='Get Started']]")

    def openPage(self):
        self.get_page.goto("https://docs.pytest.org/en/stable/")
        self.content_loaded()
        return self

    def clickGetStartedButton(self):
        self.get_started_btn.click()
        return GetStartedPage(self.get_page)\

    @staticmethod
    def testMe():
        pass

if __name__ == "__main__":
    PytestMainPage().openPage()
    PytestMainPage.testMe()