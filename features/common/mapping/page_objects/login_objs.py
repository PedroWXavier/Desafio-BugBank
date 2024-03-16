from selenium.webdriver.common.by import By


class LoginObjs:
    # ELEMENTO = (By, Locator, Descricao)
    CAMPO_EMAIL = (By.NAME, 'email')
    CAMPO_SENHA = (By.NAME, 'password')
    BOTAO_ACESSAR = (By.XPATH, '//form/div[3]/button[1]')
    BOTAO_REGISTRAR = (By.XPATH, '//form/div[3]/button[2]')
