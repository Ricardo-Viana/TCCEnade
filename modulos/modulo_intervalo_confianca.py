import pandas as pd
from operacoes.intervaloConfiancaMediaEnade import intervaloConfiancaMediaEnade

def modulo_intervalo_confianca():
    tabela_intervalo_confianca = pd.read_csv('tabelasCriadas/tabela_relacionada_conceito_cod_geral.csv', decimal=',')

    tabela_intervalo_confianca = intervaloConfiancaMediaEnade(tabela_intervalo_confianca)

    tabela_intervalo_confianca = tabela_intervalo_confianca.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_intervalo_confianca.to_csv("tabelasCriadas/intervalo_Confianca_Enade.csv", index=False)