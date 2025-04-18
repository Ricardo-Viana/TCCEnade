import pandas as pd

def calcular_correlacao(tabela):

    resultado_correlacao = []

    colunas_para_remover = ["CO_CURSO", "CO_GRUPO", "cod_geral", 'CO_CATEGAD', 'CO_ORGACAD', 'CO_MODALIDADE', 'CO_REGIAO_CURSO']

    conceito_enade = 'Conceito Enade (Contínuo)'

    tabela = tabela.drop(columns = colunas_para_remover)

    tabela = tabela.dropna(subset=[conceito_enade])

    for coluna in tabela.columns:
        if coluna != conceito_enade:
            correlacao = tabela[conceito_enade].corr(tabela[coluna])
            resultado_correlacao.append([conceito_enade, coluna, correlacao])

    tabela_correlacao = pd.DataFrame(resultado_correlacao, columns=['Conceito Enade', 'Questão', 'Correlação'])

    return tabela_correlacao
