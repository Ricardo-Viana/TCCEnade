import pandas as pd

from operacoes.relacaoCodGeral import relacionarTabelasCodGeral


def modulo_relacionar_codGeral(anos_list):
    tabela_relacionada = pd.read_csv("tabelasCriadas/tabela_relacionada_conceito.csv", decimal=',')

    for ano in anos_list:
        tabela_relacionada = relacionarTabelasCodGeral(tabela_relacionada, ano)

    tabela_relacionada['cod_geral'] = tabela_relacionada[[f'cod_geral_{ano}' for ano in anos_list]].bfill(axis=1).iloc[:, 0]

    tabela_relacionada = tabela_relacionada.drop(columns=[f'cod_geral_{ano}' for ano in anos_list])

    tabela_relacionada = tabela_relacionada.drop(columns=[f'cod_enade_{ano}' for ano in anos_list])

    tabela_relacionada = tabela_relacionada.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_relacionada.to_csv("tabelasCriadas/tabela_relacionada_conceito_cod_geral.csv", index=False)
