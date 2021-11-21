import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class E2ETest(unittest.TestCase):
    def setUp(self):
        """Sets up the browser driver and parameters."""
        browser_option = Options()
        browser_option.driver_path = "./"
        browser_option.headless = True
        self.browser = webdriver.Firefox(options=browser_option)
        self.browser.implicitly_wait(10)
        self.url = "https://www.beatsets.info/"

    def test_click_list(self):
        """Check whether clicking on the list link leads to the listing page."""
        self.browser.get(self.url)
        list_link_element = self.browser.find_element(by=By.CSS_SELECTOR, value=".nav-link.px-2.nav-text"
                                                                                ".hvr-underline-from-center")
        list_link_element.click()
        self.assertEqual(self.url + "listing", self.browser.current_url)

    def test_click_collection_card(self):
        """Check whether clicking on the collection card on the landing page or the listing page
        leads to its designated page.
        """
        # Click the first card on the landing page.
        self.browser.get(self.url)
        collection_name_element = self.browser.find_element(by=By.CSS_SELECTOR, value=".card-title.text-primary")
        # Store the clicked collection's name for further comparison.
        collection_name_text = collection_name_element.text
        collection_name_element.click()
        collection_page_title = self.browser.find_element(by=By.CSS_SELECTOR,
                                                          value=".display-5.fw-bold.text-break.aos-init.aos-animate")
        self.assertEqual(collection_name_text, collection_page_title.text)

        # Click the first card on the listing page.
        self.browser.get(self.url + "listing")
        collection_name_element = self.browser.find_element(by=By.CSS_SELECTOR, value=".card-title.text-primary")
        collection_name_text = collection_name_element.text
        collection_name_element.click()
        collection_page_title = self.browser.find_element(by=By.CSS_SELECTOR,
                                                          value=".display-5.fw-bold.text-break.aos-init.aos-animate")
        self.assertEqual(collection_name_text, collection_page_title.text)

    def test_click_collection_card_user(self):
        """Check whether clicking on the collection card's owner name leads to the user's profile page."""
        # Click the first card's owner on the landing page.
        self.browser.get(self.url)
        collection_owner_element = self.browser.find_element(by=By.CSS_SELECTOR,
                                                             value=".hvr-picture-bounce.text-decoration-none"
                                                                   ".spacing-hover")
        # Store the clicked collection owner's name for further comparison.
        collection_owner_text = collection_owner_element.text
        collection_owner_element.click()
        collection_owner_page_title = self.browser.find_element(by=By.XPATH, value="/html/body/main/div[2]/div/div["
                                                                                   "2]/h1")
        self.assertEqual(collection_owner_text, collection_owner_page_title.text)

        # Click the first card's owner on the listing page.
        self.browser.get(self.url)
        collection_owner_element = self.browser.find_element(by=By.CSS_SELECTOR,
                                                             value=".hvr-picture-bounce.text-decoration-none"
                                                                   ".spacing-hover")
        collection_owner_text = collection_owner_element.text
        collection_owner_element.click()
        collection_owner_page_title = self.browser.find_element(by=By.XPATH, value="/html/body/main/div[2]/div/div["
                                                                                   "2]/h1")
        self.assertEqual(collection_owner_text, collection_owner_page_title.text)

    def tearDown(self):
        """Closes the browser."""
        self.browser.quit()
