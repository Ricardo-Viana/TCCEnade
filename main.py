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

    modulo_metricas(anos_list)

    modulo_relacionar_conceito(anos_list)

    modulo_relacionar_codGeral(anos_list)
    
    modulo_correlacao()

    modulo_gerar_grafico(anos_list)

if __name__ == '__main__':
    main()


