### Pré-Requisito
    Ter pelo menos o python 3.10 instalado.

### Como Executar Localmente
    Basta executar a main.py para que o cenario do teste solicitado seja executado.
    Execute o seguinte por linha de comando, na raiz do projeto:
        'pip install -r requirements.txt'
        'python main.py'

### Allure-Reports
    O projeto foi configurado para gerar relatorios dos testes com o Allure reports, ao rodar os testes eh
    criado um json com os resultados na pasta allure-results.
    
    Posteriormente, esses resultados sao convertidos em um html usando as pipelines do github actions.

### Git-Hub Actions
    Foi criada uma pipeline simples no github actions que faz o seguinte:
        - Configura um ambiente linux para executar os testes com selenium (instala python, chromium e dependencias)
        - Roda os testes passando 'git' como parametro, para que eles rodem com uma configuracao apropriada para o ubuntu(python main.py git)
        - Apos rodar os testes faz um push para a branch master dos arquivos json gerados, para a pasta allure-results
        - Entao roda os jobs do Allure reports para gerar um relatorio, e, apos isso, uma pipe de deploy roda automaticamente 
          e libera os resultados na branch gh-pages.

### Como rodar a pipeline:
    Ela roda automaticamente ao subir qualquer alteracao, para rodar manualmente, va em Actions, entao va para o 
    workflow 'Test Run and Allure Report Generation' e clique em Run Workflow e confirmar.
    
    Entao basta esperar o fim da execucao, todos os passos podem ser vistos nos logs que vao sendo gerados.
    Lembrando que o deploy rodara automaticamente para liberar o relatorio do Allure.
    Para rodar todos os jobs dos dois pipes leva cerca de 5 minutos.

### Resultados 
    Ao entrar no job de deploy, eh liberado um link para o html com os reultados dos testes com o layout padrao do Allure.
    Basta acessar o link 'https://pedrowxavier.github.io/Desafio-BugBank' para ver os resultados.
    Foram deixadas algumas execucoes com inclusive uma falha para podermos visualizar nos relatorios gerados, 
    ja o log completo se encontra apenas na execucao do pipe. 
    
    Obs: Por vezes o link liberado pelo git demora para ser atualizado e nao leva ao relatorio mais atual, para isso basta acessar
    pelo link acima. 