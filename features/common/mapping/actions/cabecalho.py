from features.common.mapping.actions.base_page import BasePage
from features.common.mapping.page_objects.cabecalho_objs import CabecalhoObjs


class Cabecalho(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_no_botao_home(self):
        self._click(CabecalhoObjs.BOTAO_HOME)

    def clicar_no_sair(self):
        self._click(CabecalhoObjs.BOTAO_SAIR)
