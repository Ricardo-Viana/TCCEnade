from mediaPorCurso import processa_respostas
from relacionarConceito import relacionarTabelasConceito
from relacionarCodGeral import relacionarTabelasCodGeral
import pandas as pd
import numpy as np

def main():

    anos_input = input("Digite os anos a serem analisados (separados por vírgula, ex: 2019,2021,2022): ")
    anos_list = [int(ano.strip()) for ano in anos_input.split(',')]

    valores_na_input = input("Digite os valores a serem substituídos por NaN (separados por vírgula, ex: '*', '.'): ")
    valores_na = [valor.strip().strip("'") for valor in valores_na_input.split(',')]

    tipo_questao = input("Digite qual tipo de questão você quer gerar um relatório (pandemia, percepção prova ou processo formativo): ").lower()

    df_cinerotulo = pd.read_csv('cinerotuloenade.csv')

    metricas = pd.DataFrame()

    # Código para gerar o primeiro dataframe que contém as médias de todos os cursos
    for ano in anos_list:
        df_enade = df_cinerotulo[f'cod_enade_{ano}'].dropna() # Alterar para uma lista circular futuramente
        for cod_grupo in df_enade:
            resultado = processa_respostas(ano, cod_grupo, valores_na, tipo_questao)
            metricas = pd.concat([metricas, resultado], ignore_index=True)

    # Substituir pontos por vírgulas nos números
    metricas = metricas.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    # Exportar o resultado
    metricas.to_csv("Metricas_todos_cursos.csv", index=False, sep=';')

    tabela_relacionada = metricas

    tabela_relacionada['CO_CURSO'] = tabela_relacionada['CO_CURSO'].astype(int)

    # Código para gerar o dataframe que relaciona as tabelas com o Conceito Enade e o cod_geral
    for ano in anos_list:
        tabela_relacionada = relacionarTabelasConceito(tabela_relacionada, ano)

    tabela_relacionada = tabela_relacionada.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_relacionada['Conceito Enade (Contínuo)'] = tabela_relacionada[[f'Conceito Enade {ano}' for ano in anos_list]].bfill(axis=1).iloc[:, 0]

    tabela_relacionada.drop(columns=[f'Conceito Enade {ano}' for ano in anos_list], inplace=True)

    # Exportar o resultado
    tabela_relacionada.to_csv("tabela_relacionada_conceito.csv", index=False, sep=';')

    tabela_relacionada['CO_GRUPO'] = tabela_relacionada['CO_GRUPO'].str.replace(',', '.').astype(float)

    for ano in anos_list:
        tabela_relacionada = relacionarTabelasCodGeral(tabela_relacionada, ano)

    tabela_relacionada['cod_geral'] = tabela_relacionada[[f'cod_geral_{ano}' for ano in anos_list]].bfill(axis=1).iloc[:, 0]

    tabela_relacionada = tabela_relacionada.drop(columns=[f'cod_geral_{ano}' for ano in anos_list])

    tabela_relacionada = tabela_relacionada.drop(columns=[f'cod_enade_{ano}' for ano in anos_list])

    tabela_relacionada = tabela_relacionada.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_relacionada.to_csv("tabela_relacionada_conceito_cod_geral.csv", index=False, sep=';')


if __name__ == '__main__':
    main()

