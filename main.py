from modulos.modulo_relacionar_codGeral import modulo_relacionar_codGeral
from modulos.modulo_relacionar_conceito import modulo_relacionar_conceito
from modulos.modulo_correlacao import modulo_correlacao
from modulos.modulo_gerar_grafico import modulo_gerar_grafico
from modulos.modulo_metricas import modulo_metricas

import pandas as pd


def main():
    #Arquivo do código enade

    anos_input = input("Digite os anos a serem analisados (separados por vírgula, ex: 2019,2021,2022): ")
    anos_list = [int(ano.strip()) for ano in anos_input.split(',')]

    if 2020 in anos_list:
        raise Exception('2020 não é um ano válido')

    GRUPO_ENADE_1 = [2004,2007,2010,2013,2016,2019]

    GRUPO_ENADE_2 = [2005,2008,2011,2014,2017,2021]

    GRUPO_ENADE_3 = [2006,2009,2012,2015,2018,2022]

    relacao_ano_grupo = {}

    for ano in anos_list:
        if ano in GRUPO_ENADE_1:
            relacao_ano_grupo[ano] = "grupo_1"
        elif ano in GRUPO_ENADE_2:
            relacao_ano_grupo[ano] = "grupo_2"        
        elif ano in GRUPO_ENADE_3:
            relacao_ano_grupo[ano] = "grupo_3"        
        else:
            raise Exception(f"Ano {ano} não foi avaliado no ENADE")
    
    modulo_metricas(anos_list, relacao_ano_grupo)

    modulo_relacionar_conceito(anos_list)

    modulo_relacionar_codGeral(anos_list, relacao_ano_grupo)
    
    modulo_correlacao()

    modulo_gerar_grafico(anos_list)

if __name__ == '__main__':
    main()


