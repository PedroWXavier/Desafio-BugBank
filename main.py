import sys

from behave import __main__ as behave_executable

from util.driver import config

if __name__ == '__main__':
    if sys.argv[1:] and sys.argv[1] == 'git':
        config.local_run = False
    behave_executable.main('features/transferencias/transferencia_entre_contas.feature  --no-capture --no-capture-stderr  --tags=-dontRun ')