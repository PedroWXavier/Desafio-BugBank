from selenium.webdriver.common.by import By


class CriarContaObjs:
    # ELEMENTO = (By, Locator, Descricao)
    CAMPO_EMAIL = (By.NAME, 'email')
    CAMPO_NOME = (By.NAME, 'name')
    CAMPO_SENHA = (By.NAME, 'password')
    CAMPO_CONFIRMAR_SENHA = (By.NAME, 'passwordConfirmation')
    TOGGLE_ADICIONAR_SALDO = (By.ID, 'toggleAddBalance')
    BOTAO_CADASTRAR = (By.XPATH, '//div[2]/form/button')
