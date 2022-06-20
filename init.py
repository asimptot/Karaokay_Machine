from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import warnings

class Setup:

    def download_chrome(chrome_options):
        warnings.filterwarnings("ignore")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1036, 674')
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })

    def play_rules_instrumental(self):
        chrome_options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        options=Setup.download_chrome(chrome_options), )
        self.browser.get('https://static.wixstatic.com/mp3/92f70c_7c577b3ae7fb49218783a8022326f11e.mp3')

    def play_rules_lyrics(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        options=Setup.download_chrome(chrome_options), )
        self.driver.get('https://static.wixstatic.com/mp3/92f70c_db6a29dd6e124b98a14e3bf256ff11b7.mp3')

    def close_browser(self):
        self.browser.close()