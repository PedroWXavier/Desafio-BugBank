from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.os_manager import ChromeType

from util.driver import config

driver = None


def driver_start():
    global driver

    if driver is None:
        print("--- Iniciando chromeDriver")
        if config.local_run:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        else:
            chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

            chrome_options = Options()
            options = [
                "--headless",
                "--disable-gpu",
                "--window-size=1920,1200",
                "--ignore-certificate-errors",
                "--disable-extensions",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
            for option in options:
                chrome_options.add_argument(option)

            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        driver.get('https://bugbank.netlify.app')

    return driver


def driver_quit():
    global driver
    if driver:
        print("--- Finalizando ChromeDriver")
        driver.quit()
        driver = None
