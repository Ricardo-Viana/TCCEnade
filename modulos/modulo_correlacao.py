import pandas as pd

from operacoes.correlacaoConceitoMedia import calcularCorrelacao

def modulo_correlacao(anos_list, cod_list):
    tabela_correlacao = pd.read_csv(f"tabelasCriadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv", decimal=',')

    tabela_correlacao = calcularCorrelacao(tabela_correlacao)

    tabela_correlacao = tabela_correlacao.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_correlacao.to_csv(f"tabelasCriadas/{anos_list}{cod_list}correlação_conceito_enade_média_questão.csv", index=False)
