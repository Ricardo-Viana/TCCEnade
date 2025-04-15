import pandas as pd
from operacoes.intervalo_confianca_media_enade_IES import intervalo_confianca_media_enade_IES

def modulo_intervalo_confianca_IES(anos_list, cod_list):
    tabela_intervalo_confianca = pd.read_csv(f'tabelas_criadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv', decimal=',')

    intervalo_confianca_media_enade_IES(tabela_intervalo_confianca, anos_list, cod_list)