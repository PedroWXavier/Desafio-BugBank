from features.common.mapping.actions.base_page import BasePage
from features.common.mapping.page_objects.login_objs import LoginObjs


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def preencher_campo_login(self, usuario):
        self._send_keys(LoginObjs.CAMPO_EMAIL, usuario)

    def preencher_campo_senha(self, senha):
        self._send_keys(LoginObjs.CAMPO_SENHA, senha)

    def realizar_login(self):
        self._click(LoginObjs.BOTAO_ACESSAR)

    def entrar_menu_crair_conta(self):
        self._click(LoginObjs.BOTAO_REGISTRAR)
