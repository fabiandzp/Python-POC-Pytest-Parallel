import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
         assert "Selenium Easy" in self.driver.title

    def test_content_text(self):
        print("Verify content on the page")
        centerText = self.driver.find_element_by_css_selector('#rso > div:nth-child(1) > div > div > div > div > div.r > a:nth-child(1) > h3').text
        assert "WELCOME TO SELENIUM EASY DEMO" == centerText

    def test_bootstrap_bar(self):
        print("Lets try with another example")
        mainMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Progress Bars')]")
        mainMenu.click()

        subMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Bootstrap Progress bar')]")
        subMenu.click()

        btnDownload = self.driver.find_element_by_id("cricle-btn")
        btnDownload.click()

        WebDriverWait(self.driver, 50).until(EC.text_to_be_present_in_element_value((By.ID, 'cricleinput'), "105"))

        elemValue = self.driver.find_element_by_id("cricleinput")
        elemVAttributealue = elemValue.get_attribute('value')
        assert elemVAttributealue == "105"

    def test_one(self):
        x = "this"
        assert 'x' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        x = "welcome"
        assert hasattr(x, 'test')