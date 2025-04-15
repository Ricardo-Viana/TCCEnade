import pandas as pd

from operacoes.teste_ANOVA_IES import calcular_teste_ANOVA

def modulo_ANOVA_informacoes_IES(anos_list, cod_list):
    tabela_informacoes_IES = pd.read_csv(f'tabelas_criadas/{anos_list}{cod_list}tabela_relacionada_conceito_cod_geral.csv', decimal=',')
        
    tabela_informacoes_IES = calcular_teste_ANOVA(tabela_informacoes_IES, anos_list, cod_list)

    tabela_informacoes_IES = tabela_informacoes_IES.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    tabela_informacoes_IES.to_csv(f"tabelas_criadas/{anos_list}{cod_list}teste_ANOVA_IES.csv", index=False)