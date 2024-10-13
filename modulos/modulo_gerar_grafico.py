import pandas as pd
from operacoes.geracaoGrafico import gerarGrafico

def modulo_gerar_grafico(anos_list, cod_list):
    tabela_correlacao = pd.read_csv("tabelasCriadas/correlação_conceito_enade_média_questão.csv", decimal=',')
    
    tabela_conceito = pd.read_csv("tabelasCriadas/tabela_relacionada_conceito_cod_geral.csv", decimal=',')

    top5_correlacoes = tabela_correlacao['Correlação'].abs().nlargest(5).index

    questao_correlacoes = tabela_correlacao.loc[top5_correlacoes, 'Questão'].tolist()

    gerarGrafico(anos_list, tabela_conceito, questao_correlacoes, cod_list)