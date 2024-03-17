from time import sleep

from behave import *

from features.common.mapping.actions.criar_conta import CriarConta
from features.common.mapping.actions.login import Login
from util.accounts.accounts_manager import AccountsManager


@given(u'que eh realizado o login com um usuario "{usuario}"')
def step_impl(context, usuario):
    context.Login = Login(context.driver)
    usuario = AccountsManager.get_conta(usuario)

    context.Login.carregar_pagina('https://bugbank.netlify.app')
    context.Login.preencher_campo_login(usuario['email'])
    context.Login.preencher_campo_senha(usuario['senha'])
    context.Login.realizar_login()


@given(u'que eh realizado o cadastro de um usuario "{usuario}"')
def step_impl(context, usuario):
    context.Login = Login(context.driver)
    context.CriarConta = CriarConta(context.driver)
    usuario = AccountsManager.get_conta(usuario)

    context.Login.carregar_pagina('https://bugbank.netlify.app')
    context.Login.entrar_menu_crair_conta()

    context.CriarConta.preencher_campo_email(usuario['email'])
    context.CriarConta.preencher_campo_nome(usuario['nome'])
    context.CriarConta.preencher_campo_senha(usuario['senha'])
    context.CriarConta.preencher_campo_confirmar_senha(usuario['senha'])
    context.CriarConta.clicar_toggle_adicionar_saldo()
    context.CriarConta.realizar_registro()
