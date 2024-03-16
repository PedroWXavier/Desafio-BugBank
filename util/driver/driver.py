from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = None


def driver_start():
    global driver

    if driver is None:
        print("--- Iniciando chromeDriver")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://bugbank.netlify.app')

    return driver


def driver_quit():
    global driver
    if driver:
        print("--- Finalizando ChromeDriver")
        driver.quit()
        driver = None
