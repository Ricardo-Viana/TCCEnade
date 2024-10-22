import pandas as pd
import scipy.stats as stats
import researchpy as rp

def calcularTesteAnova(tabela):

    tabela['CO_CATEGAD'] = tabela["CO_CATEGAD"].replace({1: 'Pública Federal', 2: 'Pública Estadual', 3: 'Pública Municipal', 4: 'Privada com fins lucrativos', 5: 'Privada sem fins lucrativos', 7: 'Especial'})

    tabela['CO_ORGACAD'] = tabela["CO_ORGACAD"].replace({10019: 'Centro Federal de Educação Tecnológica', 10020: 'Centro Universitário', 10022: 'Faculdade', 10026: 'Instituto Federal de Educação, Ciência e Tecnologia', 10028: 'Universidade'})

    tabela['CO_MODALIDADE'] = tabela["CO_MODALIDADE"].replace({0: 'EaD', 1: 'Presencial'})

    tabela['CO_REGIAO_CURSO'] = tabela["CO_REGIAO_CURSO"].replace({1: 'Região Norte', 2: 'Região Nordeste', 3: 'Região Sudeste', 4: 'Região Sul', 5: 'Região Centro-Oeste'})

    rp.summary_cont(tabela['Conceito Enade (Contínuo)'])
