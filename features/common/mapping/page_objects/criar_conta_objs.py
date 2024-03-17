from selenium.webdriver.common.by import By


class CriarContaObjs:
    # ELEMENTO = (By, Locator, Descricao)
    CAMPO_EMAIL = (By.XPATH, '//form/div[2]/input', 'Campo email do formulario da pagina para criar conta')
    CAMPO_NOME = (By.NAME, 'name', 'Campo nome do formulario da pagina para criar conta')
    CAMPO_SENHA = (By.XPATH, '//form/div[4]/div/input', 'Campo senha do formulario da pagina para criar conta')
    CAMPO_CONFIRMAR_SENHA = (By.NAME, 'passwordConfirmation',
                             'Campo confirmar senha do formulario da pagina para criar conta')
    TOGGLE_ADICIONAR_SALDO = (By.ID, 'toggleAddBalance',
                              'Toggle para adicionar saldo do formulario da pagina para criar conta')
    BOTAO_CADASTRAR = (By.XPATH, '//div[2]/form/button', 'Botao cadastrar do formulario da pagina para criar conta')
    TEXTO_USUARIO_CRIADO = (By.ID, 'modalText', 'Texto de confirmacao apos criar uma conta')
