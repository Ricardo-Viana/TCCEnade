import pandas as pd
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

from operacoes.mapeamentos_IES import mapeamento_valores

def intervalo_confianca_media_enade_IES(tabela, anos_list, cod_list):
    tabela = mapeamento_valores(tabela)

    tabela = tabela.dropna(subset=['Conceito Enade (Contínuo)'])

    colunas_ies = ["CO_CATEGAD","CO_ORGACAD","CO_MODALIDADE","CO_REGIAO_CURSO"]

    for ies in colunas_ies:
        gerar_intervalo_confianca_por_IES(tabela, ies, anos_list, cod_list)

    return

def gerar_intervalo_confianca_por_IES(tabela, ies, anos_list, cod_list):
    lista_ies_valores = tabela[ies].unique()
    intervalo_confianca = pd.DataFrame(columns=[ies, 'Média', 'Limite Inferior', 'Limite Superior', 'Erro Padrão'])

    categorias_labels = []
    medias = []
    erros = []

    for i, valor in enumerate(lista_ies_valores):
        tabela_filtrada = tabela[tabela[ies] == valor]
        lista_conceito_enade = tabela_filtrada['Conceito Enade (Contínuo)'].values.tolist()
        
        media = np.mean(lista_conceito_enade)
        erro = st.sem(lista_conceito_enade)
        
        pontos_extremos = st.norm.interval(0.95, media, erro)

        limiteInferior = float(pontos_extremos[0])
        limiteSuperior = float(pontos_extremos[1])

        intervalo_confianca.loc[i] = [valor, media, limiteInferior, limiteSuperior, erro]

        categorias_labels.append(valor)
        medias.append(media)
        erros.append(erro)

    plt.figure(figsize=(12,4))
    y = np.arange(len(categorias_labels))
    plt.errorbar(medias, y, xerr=erros, fmt='none', ecolor='black', capsize=7, elinewidth=2, linewidth=5)

    plt.scatter(medias, y, color='red', zorder=5, s=50, marker='o', edgecolor='black')

    plt.yticks(y, categorias_labels)
    plt.title(f"Intervalos de Confiança - {ies}")
    plt.ylabel(ies)
    plt.xlabel("Média do Conceito Enade (Contínuo)")

    plt.savefig(f"figuras/{anos_list}{cod_list}intervalo_confianca_{ies}.png", format='png')
    plt.close()

    intervalo_confianca.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)
    intervalo_confianca.to_csv(f"tabelas_criadas/{anos_list}{cod_list}intervalo_Confianca_Enade_{ies}.csv", index=False)

    return