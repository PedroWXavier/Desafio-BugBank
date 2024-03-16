import random

from features.common.mapping.actions.home import Home
from features.common.steps.common_steps import *
from behave import *

from features.transferencias.mapping.actions.transferencia import Transferencia


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
    context.Transferencia.preencher_campo_descricao('aiai')
    context.Transferencia.realizar_transferencia()


@then('a transferencia deve ser finalizada com um comprovante sendo gerado')
def step_impl(context):
    context.Transferencia = Transferencia(context.driver)

    sleep(2)
    context.Transferencia.valida_texto_transferencia_realizada('Transferencia realizada com sucesso')
