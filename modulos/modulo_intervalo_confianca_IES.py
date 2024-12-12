import pandas as pd
from operacoes.intervaloConfiancaMediaEnadeIES import intervaloConfiancaMediaEnadeIES

def modulo_intervalo_confianca_IES(anos_list, cod_list):
    tabela_intervalo_confianca = pd.read_csv(f'tabelasCriadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv', decimal=',')

    tabela_intervalo_confianca = intervaloConfiancaMediaEnadeIES(tabela_intervalo_confianca, anos_list, cod_list)

    tabela_intervalo_confianca = tabela_intervalo_confianca.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_intervalo_confianca.to_csv(f"tabelasCriadas/{anos_list}{cod_list}intervalo_Confianca_Enade_IES.csv", index=False)