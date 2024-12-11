import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def gerarGrafico(anos_list, cod_list, tabela, questao_correlacoes):
    
    tabela['CO_GRUPO'] = tabela['CO_GRUPO'].astype('category')

    for questao in questao_correlacoes:
        tabela_qe = tabela[['cod_geral', 'CO_CURSO', 'CO_GRUPO', 'Conceito Enade (Contínuo)', f'{questao}']]

        plt.figure(figsize=(10,6))

        sns.jointplot(
            data=tabela_qe,
            x=questao,
            y='Conceito Enade (Contínuo)',
            kind='hex'
        )

        plt.savefig(f"figuras/{anos_list}{cod_list}_{questao}.png", format='png')

        plt.close()