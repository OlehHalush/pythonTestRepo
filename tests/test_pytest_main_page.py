from playwright.sync_api import Page

from pages.get_started_page.get_started_page import GetStartedPage
from pages.get_started_page.get_started_page_verifier import GetStartedPageVerifier
from pages.main_page.pytest_main_page import PytestMainPage
from pages.main_page.pytest_main_page_verifier import PytestMainPageVerifier


class TestPytestMainPage:
    def test_open_main_page(self, open_browser):
        (PytestMainPage(open_browser)
         .openPage())

        (PytestMainPageVerifier(PytestMainPage(open_browser))
         .verifyTitle("pytest: helps you write better programs")
         .verifyLogoIsVisible())

    def test_open_get_started_page(self, open_browser):
        (PytestMainPage(open_browser)
         .openPage()
         .clickGetStartedButton())

        (GetStartedPageVerifier(GetStartedPage(open_browser))
         .verifyTitle("Get Started"))

