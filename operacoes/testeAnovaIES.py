import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

def calcularTesteAnova(tabela, anos_list, cod_list):

    tabela['CO_CATEGAD'] = tabela["CO_CATEGAD"].replace({1: 'Pública Federal', 2: 'Pública Estadual', 3: 'Pública Municipal', 
                                                         4: 'Privada com fins lucrativos', 5: 'Privada sem fins lucrativos', 7: 'Especial'})

    tabela['CO_ORGACAD'] = tabela["CO_ORGACAD"].replace({10019: 'Centro Federal de Educação Tecnológica', 10020: 'Centro Universitário', 
                                                         10022: 'Faculdade', 10026: 'Instituto Federal de Educação, Ciência e Tecnologia', 
                                                         10028: 'Universidade'})

    tabela['CO_MODALIDADE'] = tabela["CO_MODALIDADE"].replace({0: 'EaD', 1: 'Presencial'})

    tabela['CO_REGIAO_CURSO'] = tabela["CO_REGIAO_CURSO"].replace({1: 'Região Norte', 2: 'Região Nordeste', 3: 'Região Sudeste', 
                                                                   4: 'Região Sul', 5: 'Região Centro-Oeste'})

    tabela = tabela.dropna(subset=['Conceito Enade (Contínuo)'])
    
    resultado_categoria_administrativa_f, resultado_categoria_administrativa_p = stats.f_oneway(
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Pública Federal'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Pública Estadual'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Pública Municipal'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Privada com fins lucrativos'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Privada sem fins lucrativos'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_CATEGAD'] == 'Especial']
    )

    resultado_organizacao_academica_f,resultado_organizacao_academica_p  = stats.f_oneway(
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'Centro Federal de Educação Tecnológica'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'Centro Universitário'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'Faculdade'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'Instituto Federal de Educação, Ciência e Tecnologia'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_ORGACAD'] == 'Universidade']
    )

    resultado_modalidade_ensino_f,resultado_modalidade_ensino_p = stats.f_oneway(
        tabela['Conceito Enade (Contínuo)'][tabela['CO_MODALIDADE'] == 'EaD'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_MODALIDADE'] == 'Presencial']
    )

    resultado_regiao_curso_f, resultado_regiao_curso_p  = stats.f_oneway(
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Região Norte'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Região Nordeste'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Região Sudeste'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Região Sul'],
        tabela['Conceito Enade (Contínuo)'][tabela['CO_REGIAO_CURSO'] == 'Região Centro-Oeste']
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

    sns.boxplot(data=tabela, x="Conceito Enade (Contínuo)", y="CO_CATEGAD")
    plt.savefig(f"figuras/{anos_list}{cod_list}_CO_CATEGAD.png", format='png')
    plt.close()

    sns.boxplot(data=tabela, x="Conceito Enade (Contínuo)", y="CO_ORGACAD")
    plt.savefig(f"figuras/{anos_list}{cod_list}_CO_ORGACAD.png", format='png')
    plt.close()

    sns.boxplot(data=tabela, x="Conceito Enade (Contínuo)", y="CO_MODALIDADE")
    plt.savefig(f"figuras/{anos_list}{cod_list}_CO_MODALIDADE.png", format='png')
    plt.close()

    sns.boxplot(data=tabela, x="Conceito Enade (Contínuo)", y="CO_REGIAO_CURSO")
    plt.savefig(f"figuras/{anos_list}{cod_list}_CO_REGIAO_CURSO.png", format='png')
    plt.close()

    return tabela_informacoes_IES
