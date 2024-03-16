from features.common.mapping.actions.base_page import BasePage
from features.common.mapping.page_objects.home_objs import HomeObjs


class Home(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def entrar_menu_transferencia(self):
        self.click(HomeObjs.BOTAO_TRANSFERIR)
