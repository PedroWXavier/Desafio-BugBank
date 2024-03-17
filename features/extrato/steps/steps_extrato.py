
from features.common.steps.steps_common import *
from features.common.mapping.actions.cabecalho import Cabecalho
from features.common.mapping.actions.home import Home
from features.extrato.mapping.actions.extrato import Extrato


@then('deve validar o extrato do usuario atualmente logado')
def step_impl(context):
    context.Cabecalho = Cabecalho(context.driver)
    context.Home = Home(context.driver)
    context.Extrato = Extrato(context.driver)

    context.Cabecalho.clicar_no_botao_home()
    context.Home.entrar_menu_extrato()

    assert context.Extrato.valida_item_no_extrato(context.descricao, context.valor)


@then('deve validar o extrato do usuario "{usuario}" nao logado')
def step_impl(context, usuario):
    context.execute_steps(f'Dado que eh realizado o login com um usuario "{usuario}"')

    context.execute_steps(f'Entao deve validar o extrato do usuario atualmente logado')
