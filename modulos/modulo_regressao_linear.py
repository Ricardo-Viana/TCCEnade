import pandas as pd

from operacoes.regressaoLinear import calcularRegressaoLinear

def modulo_regressao_linear(anos_list, cod_list):
    tabela_regressao_linear = pd.read_csv(f'tabelasCriadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv', decimal=',')

    calcularRegressaoLinear(tabela_regressao_linear, anos_list)