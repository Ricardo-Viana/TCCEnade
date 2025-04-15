import pandas as pd
from operacoes.geracao_grafico import gerar_grafico

def modulo_gerar_grafico(anos_list, cod_list):
    tabela_correlacao = pd.read_csv(f"tabelas_criadas/{anos_list}{cod_list}correlação_conceito_enade_média_questão.csv", decimal=',')
    
    tabela_conceito = pd.read_csv(f"tabelas_criadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv", decimal=',')

    top5_correlacoes = tabela_correlacao['Correlação'].abs().nlargest(5).index

    questao_correlacoes = tabela_correlacao.loc[top5_correlacoes, 'Questão'].tolist()

    gerar_grafico(anos_list, cod_list, tabela_conceito, questao_correlacoes)