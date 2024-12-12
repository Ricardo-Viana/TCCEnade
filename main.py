import argparse

from modulos.modulo_correlacao import modulo_correlacao
from modulos.modulo_gerar_grafico import modulo_gerar_grafico
from modulos.modulo_ANOVA_informacoes_IES import modulo_ANOVA_informacoes_IES
from modulos.modulo_intervalo_confianca import modulo_intervalo_confianca
from modulos.modulo_metricas import modulo_metricas
from modulos.modulo_relacionar_codGeral import modulo_relacionar_codGeral
from modulos.modulo_relacionar_conceito import modulo_relacionar_conceito
from modulos.modulo_regressao_linear import modulo_regressao_linear
from modulos.modulo_intervalo_confianca_IES import modulo_intervalo_confianca_IES

parser = argparse.ArgumentParser(description= "Gerar análise do Enade")

parser.add_argument('-a', "--anos", nargs='+', type=int,help='Lista de Anos referentes a análise', required=True)
parser.add_argument('-v', '--valoresNa', nargs='*', help='Lista de valores para serem desconsiderados da análise (ex: "*", ".")')
parser.add_argument('-tp', '--tipoQuestao', type=str, help='Tipo de questões para analisar (pandemia, percepção prova ou processo formativo)', required=True)
parser.add_argument('-c', '--cursosEspecificos', nargs='*', type=int, help='Lista de códigos gerais para filtrar análise')

args = parser.parse_args()

def main():

    valores_na = []
    cod_list = []

    if args.valoresNa is not None:
        valores_na = args.valoresNa

    if args.cursosEspecificos is not None:
        cod_list = args.cursosEspecificos


    if 2020 in args.anos:
        raise Exception('2020 não é um ano válido')

    GRUPO_ENADE_1 = [2004,2007,2010,2013,2016,2019]

    GRUPO_ENADE_2 = [2005,2008,2011,2014,2017,2021]

    GRUPO_ENADE_3 = [2006,2009,2012,2015,2018,2022]

    relacao_ano_grupo = {}

    for ano in args.anos:
        if ano in GRUPO_ENADE_1:
            relacao_ano_grupo[ano] = "grupo_1"
        elif ano in GRUPO_ENADE_2:
            relacao_ano_grupo[ano] = "grupo_2"        
        elif ano in GRUPO_ENADE_3:
            relacao_ano_grupo[ano] = "grupo_3"        
        else:
            raise Exception(f"Ano {ano} não foi avaliado no ENADE")
    
    modulo_metricas(args.anos, cod_list, valores_na, args.tipoQuestao , relacao_ano_grupo)

    modulo_relacionar_conceito(args.anos, cod_list)

    modulo_relacionar_codGeral(args.anos, relacao_ano_grupo, cod_list)
    
    modulo_correlacao(args.anos, cod_list)

    modulo_gerar_grafico(args.anos, cod_list)

    modulo_ANOVA_informacoes_IES(args.anos, cod_list)

    modulo_intervalo_confianca(args.anos, cod_list)

    modulo_intervalo_confianca_IES(args.anos, cod_list)

    modulo_regressao_linear(args.anos, cod_list)

if __name__ == '__main__':
    main()


