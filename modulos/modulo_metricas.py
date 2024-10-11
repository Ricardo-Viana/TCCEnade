import pandas as pd

from operacoes.mediaPorCurso import processa_respostas


def modulo_metricas(anos_list):
    metricas = pd.DataFrame()

    df_cinerotulo = pd.read_csv('cinerotuloenade.csv')

    valores_na_input = input("Digite os valores a serem substituídos por NaN (separados por vírgula, ex: '*', '.'): ")
    valores_na = [converter_para_tipo_apropriado(valor) for valor in valores_na_input.split(',')]

    tipo_questao = input("Digite qual tipo de questão você quer gerar um relatório (pandemia, percepção prova ou processo formativo): ").lower()


    for ano in anos_list:
        df_enade = df_cinerotulo[f'cod_enade_{ano}'].dropna()
        for cod_grupo in df_enade:
            resultado = processa_respostas(ano, cod_grupo, valores_na, tipo_questao)
            metricas = pd.concat([metricas, resultado], ignore_index=True)

    metricas = metricas.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    metricas.to_csv("tabelasCriadas/Metricas_todos_cursos.csv", index=False)


def converter_para_tipo_apropriado(valor):
    try:
        return int(valor)
    except ValueError:
        return valor.strip().strip("'")
