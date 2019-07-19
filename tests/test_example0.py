import pytest

from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
         assert "Google" in self.driver.title

    def test_search_word_01(self):
        word = "Python"
        search = self.driver.find_element_by_name("q")
        search.send_keys(word)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        print("Verify content on the page")
        centerText = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a[1]/h3').text
        assert word in centerText
        #time.sleep(5)  # sleep for 5 seconds so you can see the results


@pytest.mark.usefixtures("setup")
class TestExampleTwo:
    def test_title(self):
         assert "Google" in self.driver.title

    def test_search_word_01(self):
        word = "Python"
        search = self.driver.find_element_by_name("q")
        search.send_keys(word)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        print("Verify content on the page")
        centerText = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a[1]/h3').text
        assert word in centerText
        #time.sleep(5)  # sleep for 5 seconds so you can see the results


@pytest.mark.usefixtures("setup")
class TestExampleThree:
    def test_title(self):
         assert "Google" in self.driver.title

    def test_search_word_01(self):
        word = "Python"
        search = self.driver.find_element_by_name("q")
        search.send_keys(word)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        print("Verify content on the page")
        centerText = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a[1]/h3').text
        assert word in centerText
        #time.sleep(5)  # sleep for 5 seconds so you can see the results

@pytest.mark.usefixtures("setup")
class TestExampleFour:
    def test_title(self):
         assert "Google" in self.driver.title

    def test_search_word_01(self):
        word = "Python"
        search = self.driver.find_element_by_name("q")
        search.send_keys(word)
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        print("Verify content on the page")
        centerText = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a[1]/h3').text
        assert word in centerText
        #time.sleep(5)  # sleep for 5 seconds so you can see the results
