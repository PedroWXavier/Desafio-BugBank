#language: pt

  Funcionalidade: Transferencia Entre Contas

    Cenario: Realizar transferencia entre contas com sucesso
      Dado que realizo o cadastro de um usuario
      E que realizo o login com um usuario
      Quando entrar na pagina de transferencia entre contas
      E realizar uma transferencia entre contas
      Entao a transferencia deve ser finalizada com um comprovante sendo gerado