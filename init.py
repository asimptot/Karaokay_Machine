import time
import glob
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os, zipfile, shutil

class Setup:

    def download_chrome(chrome_options):
        warnings.filterwarnings("ignore")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1036, 674')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        chrome_options.add_argument('--no-sandbox')

        return chrome_options

    def go_to_site(self):
        chrome_options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        options=Setup.download_chrome(chrome_options), )

        self.browser.get('https://vocali.se/en')
        time.sleep(4)

    def upload_download(self):
        for file in glob.glob("C:\\Projects\\Karaoke_Manatree\\youtube-downloader-converter\\abcdefu_original.mp3"):
            self.browser.find_element_by_xpath('//input[@type="file"]').send_keys(file)
        time.sleep(5)
        N = 8  # number of times you want to press TAB

        actions = ActionChains(self.browser)
        for _ in range(N):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()

        time.sleep(2)

        actions1 = ActionChains(self.browser)
        actions1 = actions1.send_keys(Keys.ENTER)
        actions1.perform()

        time.sleep(30)

    def unzip(self):
        dir_name = r'C:\Users\Azorlu\Downloads'
        extension = ".zip"

        os.chdir(dir_name)  # change directory from working dir to dir with files

        for item in os.listdir(dir_name):  # loop through items in dir
            if item.endswith(extension):  # check for ".zip" extension
                file_name = os.path.abspath(item)  # get full path of files
                zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
                zip_ref.extractall(dir_name)  # extract file to dir
                zip_ref.close()  # close file
                os.remove(file_name)  # delete zipped file

    def move_file(self):
        path = r"C:\Users\Azorlu\Downloads"
        for file in os.listdir(path):
            if file.endswith(".mp3"):
                src = os.path.join(path, file)
                dst = r'C:\Projects\Karaoke_Manatree\wave_compare\wavs\extracted'
                shutil.move(src, dst)

    def rename(self):
        path = r"C:\Users\Azorlu\Downloads"

        song = input('What is song''s name?\n')
        music_new_name = "C:\\Users\\Azorlu\Downloads\\" + song + "_music.mp3"
        vocal_new_name = "C:\\Users\\Azorlu\Downloads\\" + song + "_vocal.mp3"

        for file in os.listdir(path):
            if file.endswith("music.mp3"):
                os.rename(os.path.join(path, file), music_new_name)

        for file in os.listdir(path):
            if file.endswith("vocals.mp3"):
                os.rename(os.path.join(path, file), vocal_new_name)

    def close_browser(self):
        self.browser.close()