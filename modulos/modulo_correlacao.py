import pandas as pd

from operacoes.correlacao_conceito_media import calcular_correlacao

def modulo_correlacao(anos_list, cod_list):
    tabela_correlacao = pd.read_csv(f"tabelas_criadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv", decimal=',')

    tabela_correlacao = calcular_correlacao(tabela_correlacao)

    tabela_correlacao = tabela_correlacao.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_correlacao.to_csv(f"tabelas_criadas/{anos_list}{cod_list}correlação_conceito_enade_média_questão.csv", index=False)
