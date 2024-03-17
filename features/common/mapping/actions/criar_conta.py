from features.common.mapping.actions.base_page import BasePage
from features.common.mapping.page_objects.criar_conta_objs import CriarContaObjs


class CriarConta(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def preencher_campo_email(self, email):
        self._send_keys(CriarContaObjs.CAMPO_EMAIL, email)

    def preencher_campo_nome(self, nome):
        self._send_keys(CriarContaObjs.CAMPO_NOME, nome)

    def preencher_campo_senha(self, senha):
        self._send_keys(CriarContaObjs.CAMPO_SENHA, senha)

    def preencher_campo_confirmar_senha(self, senha):
        self._send_keys(CriarContaObjs.CAMPO_CONFIRMAR_SENHA, senha)

    def clicar_toggle_adicionar_saldo(self):
        self._click(CriarContaObjs.TOGGLE_ADICIONAR_SALDO)

    def realizar_registro(self):
        self._click(CriarContaObjs.BOTAO_CADASTRAR)

    def retornar_numero_conta_criada(self):
        texto = self._retorna_texto(CriarContaObjs.TEXTO_USUARIO_CRIADO)
        try:
            numero_conta = texto.split()[2].split('-')
            conta = int(numero_conta[0])
            digito = int(numero_conta[1])
            return conta, digito
        except Exception as e:
            print('Erro ao obter o numero da conta criada')
            print(e)
            assert False
