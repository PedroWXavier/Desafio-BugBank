from selenium.webdriver.common.by import By


class CriarContaObjs:
    # ELEMENTO = (By, Locator, Descricao)
    CAMPO_EMAIL = (By.XPATH, '//form/div[2]/input')
    CAMPO_NOME = (By.NAME, 'name')
    CAMPO_SENHA = (By.XPATH, '//form/div[4]/div/input')
    CAMPO_CONFIRMAR_SENHA = (By.NAME, 'passwordConfirmation')
    TOGGLE_ADICIONAR_SALDO = (By.ID, 'toggleAddBalance')
    BOTAO_CADASTRAR = (By.XPATH, '//div[2]/form/button')
    TEXTO_USUARIO_CRIADO = (By.ID, 'modalText')
