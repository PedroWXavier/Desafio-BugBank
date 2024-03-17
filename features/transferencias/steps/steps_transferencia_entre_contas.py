import random

from features.common.mapping.actions.home import Home
from features.common.steps.steps_common import *
from behave import *

from features.transferencias.mapping.actions.transferencia import Transferencia


@given(u'que eh realizado o cadastro de um usuario "{usuario}" para receber uma transferencia')
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
    conta_secundaria = context.CriarConta.retornar_numero_conta_criada()
    context.conta_secundaria_numero = conta_secundaria[0]
    context.conta_secundaria_digito = conta_secundaria[1]


@when('entrar na pagina de transferencia entre contas')
def step_impl(context):
    context.Home = Home(context.driver)

    context.Home.entrar_menu_transferencia()


@when('realizar uma transferencia entre contas para um usuario secundario')
def step_impl(context):
    context.Transferencia = Transferencia(context.driver)
    context.valor = random.randint(50, 100)

    context.Transferencia.preencher_campo_numero_conta(context.conta_secundaria_numero)
    context.Transferencia.preencher_campo_digito_conta(context.conta_secundaria_digito)
    context.Transferencia.preencher_campo_valor_transferencia(context.valor)
    context.Transferencia.preencher_campo_descricao('teste descricao')
    context.Transferencia.realizar_transferencia()


@then('deve ser validado o texto no popup de conclusao de transferencia')
def step_impl(context):
    context.Transferencia = Transferencia(context.driver)

    context.Transferencia.valida_texto_transferencia_realizada('Transferencia realizada com sucesso')
