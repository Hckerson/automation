from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

from auto.web.base import WebPage
from auto.web.elements import TrackListElement
from auto.web.locators import DiscoverPageLocator


class DiscoverPage(WebPage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.accept_cookie_consent()
        self.discover_tracklist = TrackListElement(
            self._driver.find_element(*DiscoverPageLocator.DISCOVER_RESULTS),
            self._driver,
        )

    def accept_cookie_consent(self):
        try:
            self._driver.find_element(
                *DiscoverPageLocator.COOKIE_ACCEPT_NECESSARY
            ).click()
        except NoSuchElementException:
            pass
