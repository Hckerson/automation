from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from auto.base import WebComponent
from auto.locators import TrackListLocator, TrackLocator


class TrackListElement(WebComponent):
    def __init__(self, parent: WebElement, driver: WebDriver) -> None:
        super().__init__(parent, driver)
        self.available_tracks = self._get_available_tracks()

    def load_more(self) -> None:
        view_more_button = self._driver.find_element(
            *TrackListLocator.PAGINATION_BUTTON
        )
        view_more_button.click()

        self._wait.until(EC.element_to_be_clickable(TrackListLocator.PAGINATION_BUTTON))
        self.available_tracks = self._get_available_tracks()

    def _get_available_tracks(self) -> list[TrackElement]:
        self._wait.until(
            self._track_text_loaded, message="Timeout waiting for track text to load"
        )
        all_tracks = self._driver.find_elements(*TrackListLocator.ITEM)

        return [
            TrackElement(track, self._driver)
            for track in all_tracks
            if track.is_displayed() and track.text.strip()
        ]

    def _track_text_loaded(self, driver: WebDriver) -> bool:
        return any(
            e.is_displayed() and e.text.strip
            for e in driver.find_elements(*TrackListLocator.ITEM)
        )


class TrackElement(WebComponent):
    def play(self) -> None:
        if not self.is_playing:
            self._get_play_button().click()

    def pause(self) -> None:
        if self.is_playing:
            self._get_play_button().click()

    @property
    def is_playing(self) -> bool:
        aria_label = self._get_play_button().get_attribute("aria-label")
        return "Pause" in aria_label if aria_label else False

    def _get_play_button(self) -> WebElement:
        return self._parent.find_element(*TrackLocator.PLAY_BUTTON)

    def _get_track_info(self) -> dict:
        full_url = self._parent.find_element(*TrackLocator.URL).get_attribute("href")

        clean_url = full_url.split("?")[0] if full_url else ""
        try:
            genre = self._parent.find_element(*TrackLocator.GENRE).text
        except NoSuchElementException:
            genre = ""
        return {
            "genre": genre,
            "url": clean_url,
            "album": self._parent.find_element(*TrackLocator.ALBUM).text,
            "artist": self._parent.find_element(*TrackLocator.ARTIST).text,
        }
