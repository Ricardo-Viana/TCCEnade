import scipy.stats as st
import numpy as np
import pandas as pd

def intervaloConfiancaMediaEnade(tabela):
    conceito_enade = 'Conceito Enade (Contínuo)'

    tabela = tabela.dropna(subset=[conceito_enade])

    grupos_list = tabela['CO_GRUPO'].unique()

    intervalo_confianca_por_grupo = pd.DataFrame(columns=['CO_GRUPO', 'Intervalo_Confianca'])

    for i, grupo in enumerate(grupos_list):
        tabela_filtrada_grupo = tabela[tabela['CO_GRUPO'] == grupo]
        lista_conceito_enade = tabela_filtrada_grupo['Conceito Enade (Contínuo)'].values.tolist()
        # Calculo de intervalo de confiança com 95%
        pontos_extremos = st.norm.interval(0.95, np.mean(lista_conceito_enade), st.sem(lista_conceito_enade))

        pontos_extremos = (float(pontos_extremos[0]), float(pontos_extremos[1]))

        intervalo_confianca_por_grupo.loc[i] = [grupo, pontos_extremos]


    return intervalo_confianca_por_grupo