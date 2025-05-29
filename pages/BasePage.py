from abc import ABC, abstractmethod

from playwright.sync_api import Playwright, Page, Locator


class BasePage(ABC):
    def __init__(self, page: Page):
        self.__page = page

    @property
    def get_page(self) -> Page:
        return self.__page

    # @property
    # @abstractmethod
    # def get_root(self) -> Locator:
    #     pass

    def content_loaded(self):
        self.get_page.wait_for_load_state()
        # self.get_root.wait_for()
        return self
