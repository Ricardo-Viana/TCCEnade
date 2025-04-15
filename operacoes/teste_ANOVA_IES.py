import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
from operacoes.mapeamentos_IES import mapeamento_valores

def calcular_teste_ANOVA(tabela, anos_list, cod_list):

    tabela = mapeamento_valores(tabela)

    tabela = tabela.dropna(subset=['Conceito Enade (Contínuo)'])
    
    resultado_categoria_administrativa_f, resultado_categoria_administrativa_p = stats.f_oneway(
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Pública Federal'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Pública Estadual'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Pública Municipal'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Privada CFL'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Privada SFL'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Especial']
    )

    resultado_organizacao_academica_f,resultado_organizacao_academica_p  = stats.f_oneway(
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'CFET'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'C. Universitário'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'Faculdade'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'IFECT'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'Universidade']
    )

    resultado_modalidade_ensino_f,resultado_modalidade_ensino_p = stats.f_oneway(
        tabela['Conceito Enade (Contínuo)'][tabela['CO_MODALIDADE'] == 'EaD'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_MODALIDADE'] == 'Presencial']
    )

    resultado_regiao_curso_f, resultado_regiao_curso_p  = stats.f_oneway(
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Norte'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Nordeste'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Sudeste'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Sul'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Centro-Oeste']
    )
    
    tabela_informacoes_IES = pd.DataFrame({
    'anos': [anos_list],
    'categoria_administrativa_f': [resultado_categoria_administrativa_f],
    'categoria_administrativa_p': [resultado_categoria_administrativa_p],
    'organizacao_academica_f': [resultado_organizacao_academica_f],
    'organizacao_academica_p': [resultado_organizacao_academica_p],
    'modalidade_ensino_f': [resultado_modalidade_ensino_f],
    'modalidade_ensino_p': [resultado_modalidade_ensino_p],
    'resultado_regiao_curso_f': [resultado_regiao_curso_f],
    'resultado_regiao_curso_p': [resultado_regiao_curso_p]
})
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=tabela, x="Conceito Enade (Contínuo)", y="CO_CATEGAD")
    plt.savefig(f"figuras/{anos_list}{cod_list}CO_CATEGAD.png", format='png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=tabela, x="Conceito Enade (Contínuo)", y="CO_ORGACAD")
    plt.savefig(f"figuras/{anos_list}{cod_list}CO_ORGACAD.png", format='png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=tabela, x="Conceito Enade (Contínuo)", y="CO_MODALIDADE")
    plt.savefig(f"figuras/{anos_list}{cod_list}CO_MODALIDADE.png", format='png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=tabela, x="Conceito Enade (Contínuo)", y="CO_REGIAO_CURSO")
    plt.savefig(f"figuras/{anos_list}{cod_list}CO_REGIAO_CURSO.png", format='png')
    plt.close()

    return tabela_informacoes_IES
