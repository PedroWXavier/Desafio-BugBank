from features.common.mapping.actions.base_page import BasePage
from features.common.mapping.page_objects.criar_conta_objs import CriarContaObjs


class CriarConta(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def preencher_campo_email(self, email):
        self.send_keys(CriarContaObjs.CAMPO_EMAIL, email)

    def preencher_campo_nome(self, nome):
        self.send_keys(CriarContaObjs.CAMPO_NOME, nome)

    def preencher_campo_senha(self, senha):
        self.send_keys(CriarContaObjs.CAMPO_SENHA, senha)

    def preencher_campo_confirmar_senha(self, senha):
        self.send_keys(CriarContaObjs.CAMPO_CONFIRMAR_SENHA, senha)

    def clicar_toggle_adicionar_saldo(self):
        self.click(CriarContaObjs.TOGGLE_ADICIONAR_SALDO)

    def realizar_registro(self):
        self.click(CriarContaObjs.BOTAO_CADASTRAR)
