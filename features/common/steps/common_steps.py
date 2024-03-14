from time import sleep

from behave import *

from features.common.mapping.actions.criar_conta import CriarConta
from features.common.mapping.actions.login import Login
from util.driver import driver_start


@given(u'que realizo o login com um usuario')
def step_impl(context):
    context.driver = driver_start()
    context.Login = Login(context.driver)

    context.Login.carregar_pagina('https://bugbank.netlify.app')
    context.Login.preencher_campo_login('teste@gmail.com')
    context.Login.preencher_campo_senha('1234')
    context.Login.realizar_login()

    sleep(10)


@given(u'que realizo o cadastro de um usuario')
def step_impl(context):
    context.driver = driver_start()
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
