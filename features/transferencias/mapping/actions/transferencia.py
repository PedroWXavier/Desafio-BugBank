from features.common.mapping.actions.base_page import BasePage
from features.transferencias.mapping.page_objects.transferencia_objs import TransferenciaObjs


class Transferencia(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def preencher_campo_numero_conta(self, numero_conta):
        self._send_keys(TransferenciaObjs.CAMPO_NUMERO_CONTA, numero_conta)

    def preencher_campo_digito_conta(self, digito_conta):
        self._send_keys(TransferenciaObjs.CAMPO_DIGITO_CONTA, digito_conta)

    def preencher_campo_valor_transferencia(self, valor_transferencia):
        self._send_keys(TransferenciaObjs.CAMPO_VALOR_TRANSFERENCIA, valor_transferencia)

    def preencher_campo_descricao(self, descricao):
        self._send_keys(TransferenciaObjs.CAMPO_DESCRICAO, descricao)

    def realizar_transferencia(self):
        self._click(TransferenciaObjs.BOTAO_TRANSFERIR)

    def valida_texto_transferencia_realizada(self, texto):
        texto_retornado = self._retorna_texto(TransferenciaObjs.TEXTO_TRANSFERENCIA_REALIZADA)

        assert texto in texto_retornado

