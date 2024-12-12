import pandas as pd
from operacoes.intervaloConfiancaMediaEnadeIES import intervaloConfiancaMediaEnadeIES

def modulo_intervalo_confianca_IES(anos_list, cod_list):
    tabela_intervalo_confianca = pd.read_csv(f'tabelasCriadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv', decimal=',')

    intervaloConfiancaMediaEnadeIES(tabela_intervalo_confianca, anos_list, cod_list)