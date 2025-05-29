from playwright.sync_api import expect

from pages.get_started_page.get_started_page import GetStartedPage


class GetStartedPageVerifier:
    def __init__(self, parent_page: GetStartedPage):
        self.parent_page = parent_page

    def verifyTitle(self, title: str):
        expect(self.parent_page.title).to_contain_text(title)
        return self
