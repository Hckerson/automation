import time

from selenium.webdriver import Chrome
from auto.pages import DiscoverPage

BANDCAMP_DISCOVER_URL = "https://bandcamp.com/discover/"
driver = Chrome()
driver.get(BANDCAMP_DISCOVER_URL)

page = DiscoverPage(driver)

track_1 = page.discover_tracklist.available_tracks[0]
print(track_1)
track_1.play()
# track_1.pause()

time.sleep(10)
page._driver.quit()
