from features.common.steps.common_steps import *
from behave import *


@when('entrar na pagina de transferencia entre contas')
def step_impl(context):
    print('When...')


@when('realizar uma transferencia entre contas')
def step_impl(context):
    print('When...')


@then('a transferencia deve ser finalizada com um comprovante sendo gerado')
def step_impl(context):
    print('Then...')
