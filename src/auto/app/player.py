from typing import Self

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from auto.web.pages import DiscoverPage

BANDCAMP_DISCOVER_URL = "https://bandcamp.com/discover/"


class Player:
    def __init__(self) -> None:
        self._driver = self._set_up_driver()
        self.page = DiscoverPage(self._driver)
        self.tracklist = self.page.discover_tracklist
        self._current_track = self.tracklist.available_tracks[0]

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self._driver.quit()

    def play(self, track_number=None):
        if track_number:
            self.tracklist.available_tracks[track_number - 1].play()
        self._current_track.play()

    def pause(self):
        self._current_track.pause()

    def _set_up_driver(self) -> WebDriver:
        options = Options()
        options.add_argument("--headless")
        browser = Chrome(options=options)
        browser.get(BANDCAMP_DISCOVER_URL)
        return browser
