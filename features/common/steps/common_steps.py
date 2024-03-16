from time import sleep

from behave import *

from features.common.mapping.actions.criar_conta import CriarConta
from features.common.mapping.actions.login import Login


@given(u'que eh realizado o login com um usuario principal')
def step_impl(context):
    context.Login = Login(context.driver)

    context.Login.carregar_pagina('https://bugbank.netlify.app')
    context.Login.preencher_campo_login('teste@gmail.com')
    context.Login.preencher_campo_senha('1234')
    context.Login.realizar_login()


@given(u'que eh realizado o cadastro de um usuario principal')
def step_impl(context):
    context.Login = Login(context.driver)
    context.CriarConta = CriarConta(context.driver)

    context.Login.carregar_pagina('https://bugbank.netlify.app')
    context.Login.entrar_menu_crair_conta()

    context.CriarConta.preencher_campo_email('teste@gmail.com')
    context.CriarConta.preencher_campo_nome('teste')
    context.CriarConta.preencher_campo_senha('1234')
    context.CriarConta.preencher_campo_confirmar_senha('1234')
    context.CriarConta.clicar_toggle_adicionar_saldo()
    context.CriarConta.realizar_registro()


@given(u'que eh realizado o cadastro de um usuario secundario')
def step_impl(context):
    context.Login = Login(context.driver)
    context.CriarConta = CriarConta(context.driver)

    context.Login.carregar_pagina('https://bugbank.netlify.app')
    context.Login.entrar_menu_crair_conta()

    context.CriarConta.preencher_campo_email('teste2@gmail.com')
    context.CriarConta.preencher_campo_nome('teste2')
    context.CriarConta.preencher_campo_senha('1234')
    context.CriarConta.preencher_campo_confirmar_senha('1234')
    context.CriarConta.clicar_toggle_adicionar_saldo()
    context.CriarConta.realizar_registro()
    sleep(2)
    conta_secundaria = context.CriarConta.retornar_numero_conta_criada()
    context.conta_secundaria_numero = conta_secundaria[0]
    context.conta_secundaria_digito = conta_secundaria[1]

