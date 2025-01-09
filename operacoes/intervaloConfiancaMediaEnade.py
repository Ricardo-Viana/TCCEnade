import scipy.stats as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def intervaloConfiancaMediaEnade(tabela, anos_list, cod_list):
    nota_geral = 'NT_GER'
    presenca_prova = 'TP_PR_GER'

    grupos_list = tabela['CO_GRUPO'].unique()

    intervalo_confianca_por_grupo = pd.DataFrame(columns=['CO_GRUPO', 'Média', 'Limite Inferior', 'Limite Superior'])

    media_nota_geral = pd.DataFrame(columns=['CO_GRUPO', 'Média', 'Erro Padrão da Média'])

    for ano in anos_list:
        df_respostas = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2.DADOS/microdados{ano}_arq3.txt', delimiter = ';')
        
        merged_df = pd.merge(df_respostas, tabela, on='CO_CURSO')
        merged_df = merged_df[merged_df[presenca_prova] == 555.0] # Apenas alunos com participação com respostas válidas
        
        grouped_mean = merged_df.groupby('CO_GRUPO')[nota_geral].mean().reset_index(name='Média')
        grouped_sem = merged_df.groupby('CO_GRUPO')[nota_geral].sem().reset_index(name='Erro Padrão da Média')
        grouped = pd.merge(grouped_mean, grouped_sem, on='CO_GRUPO')
        
        media_nota_geral = pd.concat([media_nota_geral, grouped], ignore_index=True)

    #Educação Física Bacharelado está em dois anos de ENADE diferentes
    media_nota_geral = media_nota_geral.groupby('CO_GRUPO').agg({ 
    'Média': 'mean',
    'Erro Padrão da Média': 'mean'
    }).reset_index()


    categorias_labels = []
    medias = []
    erros = []

    for i, grupo in enumerate(grupos_list):
        media = media_nota_geral[media_nota_geral['CO_GRUPO'] == grupo]['Média'].values[0]
        erro = media_nota_geral[media_nota_geral['CO_GRUPO'] == grupo]['Erro Padrão da Média'].values[0]

        pontos_extremos = st.norm.interval(0.95, media, erro)

        limiteInferior = float(pontos_extremos[0])
        limiteSuperior = float(pontos_extremos[1])

        intervalo_confianca_por_grupo.loc[i] = [grupo, media_nota_geral[media_nota_geral['CO_GRUPO'] == grupo]['Média'].values[0], limiteInferior, limiteSuperior]
        
        categorias_labels.append(grupo)
        medias.append(media)
        erros.append(erro)
        
    plt.figure(figsize=(12,6))
    y = np.arange(len(categorias_labels))
    plt.errorbar(medias, y, xerr=erros, fmt='none', ecolor='black', capsize=7, elinewidth=2, linewidth=5)

    plt.scatter(medias, y, color='red', zorder=5, s=50, marker='o', edgecolor='black')

    plt.yticks(y, categorias_labels)
    plt.title(f"Intervalos de Confiança - Grupos")
    plt.ylabel("Grupos de Curso")
    plt.xlabel("Média das notas gerais")

    plt.savefig(f"figuras/{anos_list}{cod_list}intervalo_confianca_grupos.png", format='png')
    plt.close()
    
    return intervalo_confianca_por_grupo