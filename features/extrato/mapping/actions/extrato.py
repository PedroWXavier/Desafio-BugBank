from features.common.mapping.actions.base_page import BasePage
from features.extrato.mapping.page_objects.extrato_objs import ExtratoObjs


class Extrato(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def valida_item_no_extrato(self, descricao, valor):
        descricoes = self._retorna_lista_textos(ExtratoObjs.DESCRICAO_ITEM_EXTRATO)
        valores = self._retorna_lista_textos(ExtratoObjs.VALOR_ITEM_EXTRATO)

        if len(descricoes) != len(valores):
            print('\t\tNumero de descricoes encontrados diferente do numero de valores encontrados no extrato')
            return False

        for i in range(0, len(descricoes)):
            if descricao in descricoes[i] and str(valor) in valores[i]:
                print(f'\t\tFoi encontrado um comprovante com o Valor: {valor} e a Descricao: {descricao}')
                return True

        return False
