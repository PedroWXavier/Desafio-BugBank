#language: pt

  Funcionalidade: Transferencia Entre Contas

    Cenario: Realizar transferencia entre contas com sucesso
      Dado que eh realizado o cadastro de um usuario principal
      E que eh realizado o cadastro de um usuario secundario
      E que eh realizado o login com um usuario principal
      Quando entrar na pagina de transferencia entre contas
      E realizar uma transferencia entre contas para um usuario secundario
      Entao a transferencia deve ser finalizada com um comprovante sendo gerado