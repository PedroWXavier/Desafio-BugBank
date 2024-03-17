from selenium.webdriver.common.by import By


class TransferenciaObjs:
    # ELEMENTO = (By, Locator, Descricao)
    CAMPO_NUMERO_CONTA = (By.NAME, 'accountNumber',
                          'Campo numero do formulario da pagina de transferencia')
    CAMPO_DIGITO_CONTA = (By.NAME, 'digit', 'Campo digito do formulario da pagina de transferencia')
    CAMPO_VALOR_TRANSFERENCIA = (By.NAME, 'transferValue', 'Campo valor do formulario da pagina de transferencia')
    CAMPO_DESCRICAO = (By.NAME, 'description', 'Campo descricao do formulario da pagina de transferencia')
    BOTAO_TRANSFERIR = (By.XPATH, '//div[3]/form/button', 'Botao transferir do formulario da pagina de transferencia')
    TEXTO_TRANSFERENCIA_REALIZADA = (By.ID, 'modalText', 'Texto de confirmacao da transferencia realizada')
    BOTAO_FECHAR_POPUP = (By.ID, 'btnCloseModal', 'Botao para fechar o popup que aparece ao concluir uma transferencia')
