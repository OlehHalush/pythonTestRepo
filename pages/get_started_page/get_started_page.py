from playwright.sync_api import Page

from pages.BasePage import BasePage


class GetStartedPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("//h1")