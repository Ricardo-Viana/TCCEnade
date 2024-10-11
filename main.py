from mediaPorCurso import processa_respostas
from relacaoConceito import relacionarTabelasConceito
from relacaoCodGeral import relacionarTabelasCodGeral
from correlacaoConceitoMedia import calcularCorrelacao
import pandas as pd
import numpy as np

def main():

    anos_input = input("Digite os anos a serem analisados (separados por vírgula, ex: 2019,2021,2022): ")
    anos_list = [int(ano.strip()) for ano in anos_input.split(',')]

    if 2020 in anos_list:
        raise Exception('2020 não é um ano válido')

    valores_na_input = input("Digite os valores a serem substituídos por NaN (separados por vírgula, ex: '*', '.'): ")
    valores_na = [converter_para_tipo_apropriado(valor) for valor in valores_na_input.split(',')]

    tipo_questao = input("Digite qual tipo de questão você quer gerar um relatório (pandemia, percepção prova ou processo formativo): ").lower()

    df_cinerotulo = pd.read_csv('cinerotuloenade.csv')

    metricas = pd.DataFrame()

    for ano in anos_list:
        df_enade = df_cinerotulo[f'cod_enade_{ano}'].dropna()
        for cod_grupo in df_enade:
            resultado = processa_respostas(ano, cod_grupo, valores_na, tipo_questao)
            metricas = pd.concat([metricas, resultado], ignore_index=True)

    metricas = metricas.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    metricas.to_csv("tabelasCriadas/Metricas_todos_cursos.csv", index=False)

    tabela_relacionada = pd.read_csv("tabelasCriadas/Metricas_todos_cursos.csv", decimal=',')

    for ano in anos_list:
        tabela_relacionada = relacionarTabelasConceito(tabela_relacionada, ano)


    tabela_relacionada['Conceito Enade (Contínuo)'] = tabela_relacionada[[f'Conceito Enade {ano}' for ano in anos_list]].bfill(axis=1).iloc[:, 0]

    tabela_relacionada.drop(columns=[f'Conceito Enade {ano}' for ano in anos_list], inplace=True)

    tabela_relacionada = tabela_relacionada.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_relacionada.to_csv("tabelasCriadas/tabela_relacionada_conceito.csv", index=False)

    tabela_relacionada = pd.read_csv("tabelasCriadas/tabela_relacionada_conceito.csv", decimal=',')

    for ano in anos_list:
        tabela_relacionada = relacionarTabelasCodGeral(tabela_relacionada, ano)

    tabela_relacionada['cod_geral'] = tabela_relacionada[[f'cod_geral_{ano}' for ano in anos_list]].bfill(axis=1).iloc[:, 0]

    tabela_relacionada = tabela_relacionada.drop(columns=[f'cod_geral_{ano}' for ano in anos_list])

    tabela_relacionada = tabela_relacionada.drop(columns=[f'cod_enade_{ano}' for ano in anos_list])

    tabela_relacionada = tabela_relacionada.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_relacionada.to_csv("tabelasCriadas/tabela_relacionada_conceito_cod_geral.csv", index=False)

    tabela_correlacao = pd.read_csv("tabelasCriadas/tabela_relacionada_conceito_cod_geral.csv", decimal=',')

    tabela_correlacao = calcularCorrelacao(tabela_correlacao)

    tabela_correlacao = tabela_correlacao.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_correlacao.to_csv("tabelasCriadas/correlação_conceito_enade_média_questão.csv", index=False)

def converter_para_tipo_apropriado(valor):
    try:
        return int(valor)
    except ValueError:
        return valor.strip().strip("'")
    
if __name__ == '__main__':
    main()


