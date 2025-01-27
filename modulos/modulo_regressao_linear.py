import pandas as pd

from operacoes.regressaoLinear import calcularRegressaoLinear

def modulo_regressao_linear(anos_list, cod_list):
    tabela_regressao_linear = pd.read_csv(f'tabelasCriadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv', decimal=',')

    tabela_regressao_linear= calcularRegressaoLinear(tabela_regressao_linear, anos_list, cod_list)

    tabela_regressao_linear = tabela_regressao_linear.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)
    
    tabela_regressao_linear.to_csv(f"tabelasCriadas/{anos_list}{cod_list}regressao_linear_OLS.csv", index=False)