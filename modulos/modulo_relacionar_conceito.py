import pandas as pd

from operacoes.relacaoConceito import relacionarTabelasConceito


def modulo_relacionar_conceito(anos_list):
    tabela_relacionada = pd.read_csv("tabelasCriadas/Metricas_todos_cursos.csv", decimal=',')

    for ano in anos_list:
        tabela_relacionada = relacionarTabelasConceito(tabela_relacionada, ano)


    tabela_relacionada['Conceito Enade (Contínuo)'] = tabela_relacionada[[f'Conceito Enade {ano}' for ano in anos_list]].bfill(axis=1).iloc[:, 0]

    tabela_relacionada.drop(columns=[f'Conceito Enade {ano}' for ano in anos_list], inplace=True)

    tabela_relacionada = tabela_relacionada.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_relacionada.to_csv("tabelasCriadas/tabela_relacionada_conceito.csv", index=False)
