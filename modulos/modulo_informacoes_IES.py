import pandas as pd

from operacoes.testeAnovaIES import calcularTesteAnova

def modulo_informacoes_IES(anos_list):
    tabela_informacoes_IES = pd.read_csv('tabelasCriadas/tabela_relacionada_conceito_cod_geral.csv', decimal=',')
        
    tabela_informacoes_IES = calcularTesteAnova(tabela_informacoes_IES, anos_list)

    tabela_informacoes_IES = tabela_informacoes_IES.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_informacoes_IES.to_csv("tabelasCriadas/teste_ANOVA_IES.csv", index=False)