import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Sunlife.com.Pages.Home_Sunlife import Sunlife_Home

baseurl = "https://www.sunlife.com/"



@pytest.fixture(scope='function', autouse=True)
def driver(request):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument(f"--window-size={1920},{3926}")
    # chrome_options.add_argument("--hide-scrollbars")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(8)
    driver.get(baseurl)
    driver.find_element_by_xpath("//button[@id='stayoncom']").click()

    def driver_teardown():
        print("closing browser")
        driver.close()

    request.addfinalizer(driver_teardown)
    yield driver


@pytest.fixture(scope='function', autouse=True)
def home(driver):
    obj = Sunlife_Home(driver)
    yield obj


@pytest.mark.usefixtures("driver", "home")
class Tests():

    def test_01_verify_url1_title(self, driver, home):
        print(home.verify_title())

    def test_02_validate_header_links_moves_to_corresponding_page(self, home):
        home.verify_headers()

    def test_03_validate_Products_mega_menu(self, driver, home):
        home.verify_megamenu_links("Sustainability")
        # driver.find_element_by_xpath("").get_attribute()

    def test_04_validate_Products_and_Services_mega_menu(self, driver, home):
        home.verify_megamenu_links("Products_and_Services")

    def test_05_validate_Investors_megamenu(self, driver, home):
        home.verify_megamenu_links("Investors_megamenu")

    def test_06_validate_About_us_mega_menu(self, driver, home):
        home.verify_megamenu_links("About_us")
#===================================================================
    def test_07_search_functionality(self, driver, home):
        home.verify_search()

    def test_08_validate_Footer_section_2(self, driver, home):
        home.verify_footer_quicklinks("footer_section_2", breadcrumb_status=True)

    def test_09_validate_Footer_section_1(self, driver, home):
        home.verify_footer_quicklinks("footer_section_1")


if __name__ == '__main__':
    pytest.main()
