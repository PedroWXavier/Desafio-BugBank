from selenium.webdriver.common.by import By


class CabecalhoObjs:
    BOTAO_HOME = (By.XPATH, '//div/div[1]/a', 'Botao para voltar a Home do cabecalho')
    BOTAO_SAIR = (By.ID, 'btnExit', 'Botao para sair da conta do cabecalho')
