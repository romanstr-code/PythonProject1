# Open browser
# selenium 4
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #adding delay in time to observe the run
        time.sleep(3)

        # 1. Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        #adding delay in time to observe the run
        time.sleep(2)

        # 2. Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # 3. Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # 4. Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # 5. Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # 6. Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # 7 . Verify button Log out is displayed on the new page
        log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_button_locator.is_displayed()


