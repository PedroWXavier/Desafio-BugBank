from selenium.webdriver.common.by import By


class LoginObjs:
    # ELEMENTO = (By, Locator, Descricao)
    CAMPO_EMAIL = (By.NAME, 'email', 'Campo email do formulario da pagina de Login')
    CAMPO_SENHA = (By.NAME, 'password', 'Campo senha do formulario da pagina de Login')
    BOTAO_ACESSAR = (By.XPATH, '//form/div[3]/button[1]', 'Botao acessar da pagina de Login')
    BOTAO_REGISTRAR = (By.XPATH, '//form/div[3]/button[2]', 'Botao registrar da pagina de Login')
