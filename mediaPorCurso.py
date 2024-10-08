import pandas as pd
import numpy as np

def processa_respostas(ano, cod_grupo, prefixo_coluna, valores_na, caminho_base):
    df = pd.read_csv(f'{caminho_base}/Microdados{ano}/microdados{ano}_arq1.txt', delimiter=';')
    filtered_df = df[df['CO_GRUPO'] == cod_grupo]
    unique_courses = filtered_df['CO_CURSO'].unique()
    df_respostas = pd.read_csv(f'{caminho_base}/Microdados{ano}/microdados{ano}_arq3.txt', delimiter=';')

    # Filtrar cursos únicos
    df_respostas_filtered = df_respostas[df_respostas['CO_CURSO'].isin(unique_courses)]

    # Identificar as colunas de respostas com base no prefixo fornecido
    colunas_respostas = [col for col in df_respostas_filtered.columns if col.startswith(prefixo_coluna)]

    # Substituir valores por escala de 1 a 5
    df_respostas_filtered[colunas_respostas] = df_respostas_filtered[colunas_respostas].replace({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5})

    # Substituir valores não numéricos por NaN
    df_respostas_filtered[colunas_respostas] = df_respostas_filtered[colunas_respostas].replace(valores_na, np.nan)

    # Remover linhas onde todas as respostas são NaN
    df_respostas_filtered = df_respostas_filtered.dropna(how='all', subset=colunas_respostas)

    # Calcular a média das respostas por curso
    media_respostas = df_respostas_filtered.groupby('CO_CURSO')[colunas_respostas].mean().reset_index()

    # Adicionar a coluna 'CO_GRUPO' ao resultado
    media_respostas['CO_GRUPO'] = cod_grupo

    return media_respostas

# Solicitar entrada do usuário para os anos a serem analisados
anos_input = input("Digite os anos a serem analisados (separados por vírgula, ex: 2019,2021,2022): ")
anos_list = [int(ano.strip()) for ano in anos_input.split(',')]

# Solicitar entrada do usuário para os valores a serem substituídos por np.nan
valores_na_input = input("Digite os valores a serem substituídos por NaN (separados por vírgula, ex: '*', '.'): ")
valores_na = [valor.strip().strip("'") for valor in valores_na_input.split(',')]

# Carregar o arquivo base com os códigos de grupo
df_cinerotulo = pd.read_csv('/content/drive/MyDrive/TCCENADEARQUIVOS/cinerotuloenade.csv')

# Criar DataFrame para consolidar as métricas
metricas = pd.DataFrame()

# Caminho base para os arquivos de microdados
caminho_base = '/content/drive/MyDrive/TCCENADEARQUIVOS'

# Processar para cada ano e grupo
for ano in anos_list:
    if ano in anos_colunas:
        df_enade = df_cinerotulo[f'cod_enade_{ano}'].dropna()
        for cod_grupo in df_enade:
            resultado = processa_respostas(ano, cod_grupo, anos_colunas[ano], valores_na, caminho_base)
            metricas = pd.concat([metricas, resultado], ignore_index=True)
    else:
        print(f"Ano {ano} não está disponível para análise.")

# Substituir pontos por vírgulas nos números
metricas = metricas.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

# Exportar o resultado
metricas.to_csv("Metricas_todos_cursos.csv", index=False, sep=';')