from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait_time_out = 5
        self._retentativas = 5

    def carregar_pagina(self, link):
        self._driver.get(link)

    def _click(self, by_locator, retentativas=None, wait=False, wait_time_out=None):
        if wait_time_out is None:
            wait_time_out = self._wait_time_out
        if retentativas is None:
            retentativas = self._retentativas

        erro = None
        for i in range(retentativas):
            try:
                if wait:
                    WebDriverWait(self._driver, wait_time_out).until(
                        expected_conditions.element_to_be_clickable((by_locator[0], by_locator[1]))).click()
                else:
                    self._driver.find_element(by_locator[0], by_locator[1]).click()
                print(f'\t\tClicou no elemento \n\t\t\t{self.__format_locator(by_locator)}')
                return
            except Exception as e:
                erro = e
                sleep(1)
        print(f'\t\tErro ao clicar no elemento \n\t\t\t{self.__format_locator(by_locator)}')
        raise erro

    def _send_keys(self, by_locator, keys, retentativas=None, wait=False, wait_time_out=None):
        if wait_time_out is None:
            wait_time_out = self._wait_time_out
        if retentativas is None:
            retentativas = self._retentativas

        erro = None
        for i in range(retentativas):
            try:
                if wait:
                    WebDriverWait(self._driver, wait_time_out).until(
                        expected_conditions.visibility_of_element_located(
                            (by_locator[0], by_locator[1]))).send_keys(keys)
                else:
                    self._driver.find_element(by_locator[0], by_locator[1]).send_keys(keys)
                print(f'\t\tDigitou {keys} no campo \n\t\t\t{self.__format_locator(by_locator)}')
                return
            except Exception as e:
                erro = e
                sleep(1)
        print(f'\t\tErro ao digitar {keys} no campo \n\t\t\t{self.__format_locator(by_locator)}')
        raise erro

    def _retorna_texto(self, by_locator, retentativas=None):
        if retentativas is None:
            retentativas = self._retentativas

        erro = None
        for i in range(retentativas):
            try:
                text = self._driver.find_element(by_locator[0], by_locator[1]).text
                if text:
                    print(f'\t\tEncontrou {text} no campo \n\t\t\t{self.__format_locator(by_locator)}')
                    return text
                else:
                    sleep(1)
            except Exception as e:
                erro = e
                sleep(1)
        print(f'\t\tErro ao procurar texto no campo \n\t\t\t{self.__format_locator(by_locator)}')
        raise erro

    def __format_locator(self, by_locator):
        return f'(By: {by_locator[0]} | Locator: {by_locator[1]} | Descricao: {by_locator[2]})'
