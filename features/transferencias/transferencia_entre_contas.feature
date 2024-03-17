#language: pt

  Funcionalidade: Transferencia Entre Contas

    Cenario: Realizar transferencia entre contas com sucesso
      Dado que eh realizado o cadastro de um usuario "principal"
      E que eh realizado o cadastro de um usuario "secundario" para receber uma transferencia
      E que eh realizado o login com um usuario "principal"
      Quando entrar na pagina de transferencia entre contas
      E realizar uma transferencia entre contas para um usuario secundario
      Entao deve ser validado o texto no popup de conclusao de transferencia
      E deve validar o extrato do usuario atualmente logado
      E deve validar o extrato do usuario "secundario" nao logado