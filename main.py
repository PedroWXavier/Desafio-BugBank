from behave import __main__ as behave_executable

if __name__ == '__main__':
    behave_executable.main('features/transferencias/transferencia_entre_contas.feature  --no-capture --no-capture-stderr  '
                           '--tags=-dontRun ')

