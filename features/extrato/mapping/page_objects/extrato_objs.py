from selenium.webdriver.common.by import By


class ExtratoObjs:
    DESCRICAO_ITEM_EXTRATO = (By.ID, 'textDescription', 'Descricao de um item do extrato')
    VALOR_ITEM_EXTRATO = (By.ID, 'textTransferValue', 'Valor de um item do extrato')
