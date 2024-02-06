import os

from selenium import webdriver
from selenium.common import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


class SetupDriver:
    @staticmethod
    def path_to_chrome():
        return ChromeDriverManager().install()

    @staticmethod
    def setup_driver(cmd_browser=None, request=None, path_to_driver=None):
        options = Options()
        path = os.path.join(".", "source_downloaded")
        prefs = {"download.default_directory": os.path.abspath(path)}
        options.add_experimental_option("prefs", prefs)
        if request and request.config.getoption('--visible') == "False":
            """Если режим без браузера"""
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--remote-debugging-port=9222')
            options.add_argument('--enable-javascript')
            options.add_argument('--no-sandbox')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--allow-insecure-localhost')
            options.add_argument("--window-size=1920,1080")
            options.add_argument('--disable-setuid-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--start-maximized")
            # options.add_argument('--window-size=1420,1080')

        try:
            driver = webdriver.Chrome(service=ChromeService(executable_path=path_to_driver), options=options)\
                if path_to_driver else webdriver.Chrome(options=options)
            driver.maximize_window()
            driver.implicitly_wait(10)
            return driver

        except WebDriverException:
            raise WebDriverException("Ошибка установки драйвера")
