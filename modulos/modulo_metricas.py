import pandas as pd

from operacoes.mediaPorCurso import processa_respostas


def modulo_metricas(anos_list, cod_list, valores_na, tipo_questao, relacao_ano_grupo):
    metricas = pd.DataFrame()

    df_cinerotulo = pd.read_csv('cinerotuloenade.csv')

    valores_na = [converter_para_tipo_apropriado(valor) for valor in valores_na]

    for ano in anos_list:
        df_enade = df_cinerotulo[f'cod_enade_{relacao_ano_grupo[ano]}'].dropna() 
        for cod_grupo in df_enade:
            resultado = processa_respostas(ano, cod_grupo, valores_na, tipo_questao)
            metricas = pd.concat([metricas, resultado], ignore_index=True)

    metricas = metricas.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, (float, int)) else x)

    metricas.to_csv(f"tabelasCriadas/{anos_list}{cod_list}metricas_todos_cursos.csv", index=False)


def converter_para_tipo_apropriado(valor):
    try:
        return int(valor)
    except ValueError:
        return valor.strip().strip("'")
