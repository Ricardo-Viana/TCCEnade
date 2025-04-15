import pandas as pd

from operacoes.relacao_cod_geral import relacionar_tabelas_cod_geral

def modulo_relacionar_codGeral(anos_list, relacao_ano_grupo, cod_list):
    tabela_relacionada = pd.read_csv(f"tabelas_criadas/{anos_list}{cod_list}tabela_relacionada_conceito.csv", decimal=',')

    for ano in anos_list:
        tabela_relacionada = relacionar_tabelas_cod_geral(tabela_relacionada, relacao_ano_grupo[ano])

    tabela_relacionada['cod_geral'] = tabela_relacionada[[f'cod_geral_{relacao_ano_grupo[ano]}' for ano in anos_list]].bfill(axis=1).iloc[:, 0]

    tabela_relacionada = tabela_relacionada.drop(columns=[f'cod_geral_{relacao_ano_grupo[ano]}' for ano in anos_list])

    tabela_relacionada = tabela_relacionada.drop(columns=[f'cod_enade_{relacao_ano_grupo[ano]}' for ano in anos_list])

    if len(cod_list) > 0:
        tabela_relacionada = tabela_relacionada[tabela_relacionada['cod_geral'].isin(cod_list)]

    tabela_relacionada = tabela_relacionada.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_relacionada.to_csv(f"tabelas_criadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv", index=False)