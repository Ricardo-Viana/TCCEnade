import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def gerar_grafico(anos_list, cod_list, tabela, questao_correlacoes):
    
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
        
        tabela['CO_GRUPO'] = tabela['CO_GRUPO'].astype('category')

    num_questoes = len(questao_correlacoes)
    cols = 3
    rows = math.ceil(num_questoes / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 5))
    axes = axes.flatten()

    for i, questao in enumerate(questao_correlacoes):
        tabela_qe = tabela[['cod_geral', 'CO_CURSO', 'CO_GRUPO', 'Conceito Enade (Contínuo)', questao]]

        sns.regplot(
            data=tabela_qe,
            x=questao,
            y='Conceito Enade (Contínuo)',
            scatter_kws={'s': 30, 'alpha': 0.4}, 
            line_kws={'color': 'red'}, 
            ax=axes[i], 
            fit_reg=True 
        )

        axes[i].set_title(f"Questão: {questao}")
        axes[i].legend().remove()

    
    for j in range(num_questoes, len(axes)):
        axes[j].axis('off')

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, title="CO_GRUPO", loc='upper right')

    plt.tight_layout()
    plt.savefig(f"figuras/{anos_list}{cod_list}todas_questoes_regplot.png", format='png', bbox_inches='tight')
    plt.close()