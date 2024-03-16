from selenium.webdriver.common.by import By


class TransferenciaObjs:
    # ELEMENTO = (By, Locator, Descricao)
    CAMPO_NUMERO_CONTA = (By.NAME, 'accountNumber')
    CAMPO_DIGITO_CONTA = (By.NAME, 'digit')
    CAMPO_VALOR_TRANSFERENCIA = (By.NAME, 'transferValue')
    CAMPO_DESCRICAO = (By.NAME, 'description')
    BOTAO_TRANSFERIR = (By.XPATH, '//div[3]/form/button')
    TEXTO_TRANSFERENCIA_REALIZADA = (By.ID, 'modalText')
