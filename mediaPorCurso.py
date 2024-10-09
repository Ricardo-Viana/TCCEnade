import pandas as pd
import numpy as np
import requests
from io import BytesIO
from zipfile import ZipFile
import os
import re

def processa_respostas(ano, cod_grupo, valores_na, tipo_questao):
    if ano == 2021:
        url = 'https://download.inep.gov.br/microdados/microdados_enade_2021.zip'
    else:
        url = f'https://download.inep.gov.br/microdados/microdados_enade_{ano}_LGPD.zip'

    dir_path = f'./enade{ano}'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
    if not os.listdir(dir_path):
    
        filebytes = BytesIO(
            requests.get(url).content
        )

        myzip = ZipFile(filebytes)
        myzip.extractall(dir_path)
        for root, dirs, files in os.walk(f'enade{ano}/microdados_Enade_{ano}_LGPD'):
        # Normaliza os diretórios
            for dir_name in dirs:
                new_dir_name = dir_name.replace(' ', '')
                old_path = os.path.join(root, dir_name)
                new_path = os.path.join(root, new_dir_name)
                os.rename(old_path, new_path)
    
    df = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2.DADOS/microdados{ano}_arq1.txt', delimiter = ';')
    filtered_df = df[df['CO_GRUPO'] == cod_grupo]
    unique_courses = filtered_df['CO_CURSO'].unique()

    if tipo_questao == 'pandemia':
        
        if ano >= 2021:
            files = os.listdir(f'enade{ano}/microdados_Enade_{ano}/2.DADOS')
            files_sorted_by_number = sorted(files, key=lambda x: int(re.search(fr'microdados{ano}_arq(\d+)', x).group(1)))
            latest_file = files_sorted_by_number[-1]    
            df_respostas = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2.DADOS/{latest_file}', delimiter = ';')
        else:
            raise Exception('Ano não está incluso na pandemia')

        df_respostas_filtered = df_respostas[df_respostas['CO_CURSO'].isin(unique_courses)]

        colunas_respostas = [col for col in df_respostas_filtered.columns if col.startswith('QE_')]

        novos_nomes_colunas = [f"QE_{i+1}" for i in range(len(colunas_respostas))]

        renomear_dict = dict(zip(colunas_respostas, novos_nomes_colunas))

        df_respostas_filtered.rename(columns=renomear_dict, inplace=True)

        colunas_respostas = novos_nomes_colunas

    elif tipo_questao == 'percepção prova':

        df_respostas = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2.DADOS/microdados{ano}_arq3.txt', delimiter = ';')
        
        df_respostas_filtered = df_respostas[df_respostas['CO_CURSO'].isin(unique_courses)]

        colunas_respostas = [col for col in df_respostas_filtered.columns if col.startswith('CO_RS')]

        df_respostas_filtered[colunas_respostas] = df_respostas_filtered[colunas_respostas].replace({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5})


    elif tipo_questao == 'processo formativo':
        
        df_respostas = pd.read_csv(f'enade{ano}/microdados_Enade_{ano}_LGPD/2.DADOS/microdados{ano}_arq4.txt', delimiter = ';')

        df_respostas_filtered = df_respostas[df_respostas['CO_CURSO'].isin(unique_courses)]

        colunas_respostas = [col for col in df_respostas_filtered.columns if col.startswith('QE_')]
        
    df_respostas_filtered[colunas_respostas] = df_respostas_filtered[colunas_respostas].replace(valores_na, np.nan)

    df_respostas_filtered = df_respostas_filtered.dropna(how='all', subset=colunas_respostas)

    media_respostas = df_respostas_filtered.groupby('CO_CURSO')[colunas_respostas].mean().reset_index()

    media_respostas['CO_GRUPO'] = cod_grupo

    return media_respostas