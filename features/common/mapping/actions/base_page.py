from time import sleep


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.time_out = 15
        self.retentativas = 5

    def carregar_pagina(self, link):
        self.driver.get(link)

    def click_element_impl(self, by_locator):
        self.driver.find_element(by_locator[0], by_locator[1]).click()
        print("clicou - %s" % (by_locator[1]))
        return True

    def click(self, by_locator, retentativas=None, obrigatorio=True, tentar_scroll=False):
        if retentativas is None:
            retentativas = self.retentativas

        err = None
        for i in range(retentativas):
            try:
                self.click_element_impl(by_locator)
                return
            except Exception as e:
                err = e
            sleep(1)

        if err is not None and tentar_scroll:
            print("clicou falhou, tentando scroll - %s" % (by_locator[1]))
            for i in range(7):
                self.driver.swipe(200, 400, 150, 200, 1000)
                try:
                    self.click_element_impl(by_locator)
                    return
                except Exception as e:
                    err = e

        if obrigatorio and err is not None:
            raise err

    def send_keys(self, by_locator, keys, retentativas=None, obrigatorio=True):
        if retentativas is None:
            retentativas = self.retentativas

        err = None
        for i in range(retentativas):
            try:
                self.driver.find_element(by_locator[0], by_locator[1]).send_keys(keys)
                print("digitou - %s |%s" % (keys, by_locator[1]))
                return
            except Exception as e:
                err = e
                self.exception_deve_retentar(err)
                sleep(1)
        if obrigatorio and err is not None:
            raise err
