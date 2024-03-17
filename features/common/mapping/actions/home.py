from features.common.mapping.actions.base_page import BasePage
from features.common.mapping.page_objects.home_objs import HomeObjs


class Home(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def entrar_menu_transferencia(self):
        self._click(HomeObjs.BOTAO_TRANSFERIR, wait=True)

    def entrar_menu_extrato(self):
        self._click(HomeObjs.BOTAO_EXTRATO, wait=True)
