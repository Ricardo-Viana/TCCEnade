import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import RFE

def calcularRegressaoLinear(tabela, anos_list):

    preditores = [col for col in tabela.columns if col.startswith('QE_I')]
    resultado = 'Conceito Enade (Contínuo)'

    tabela = tabela.dropna(subset=[resultado]) # Tirar conceito enade que tinham valores nulos
    
    for questao in preditores:
        tabela = tabela.dropna(subset=[questao]) # Tirar as questões que tinham valores nulos
    
    RMSE, r2 = regressaoLinearSkLearn(tabela, preditores, resultado, anos_list)
    print(f'Root Mean Square Error (RMSE): {RMSE:.0f}')
    print(f'Coeficiente de determinação (r2): {r2:.4f}')

    resultado = regressaoLinearStModel(tabela, preditores, resultado)
    print(resultado.summary())

    return


def regressaoLinearSkLearn(tabela, preditores, resultado, anos_list):
    questoes_lm = LinearRegression()
    questoes_lm.fit(tabela[preditores], tabela[resultado])

    treinado = questoes_lm.predict(tabela[preditores])
    RMSE = np.sqrt(mean_squared_error(tabela[resultado], treinado))
    r2 = r2_score(tabela[resultado], treinado)

    scores = []
    n_features_lst = range(1, len(tabela[preditores].columns))
    for n_features in n_features_lst:
        selector = RFE(questoes_lm, n_features_to_select=n_features, step=1)
        selector = selector.fit(tabela[preditores], tabela[resultado])
        scores.append(selector.score(tabela[preditores], tabela[resultado]))
        

    plt.plot(n_features_lst, scores, color='red')
    plt.xlabel("N features")
    plt.ylabel("R2")
    plt.ylim([0, 0.4])
    plt.xlim([0, 41])
    plt.title("Regressão Linear")
    plt.savefig(f"figuras/{anos_list}_regressao_rfe.png", format='png')
    plt.close()

    return RMSE, r2


def regressaoLinearStModel(tabela, preditores, resultado):
    modelo = sm.OLS(tabela[resultado], tabela[preditores].assign(const=1))
    resultado = modelo.fit()

    return resultado