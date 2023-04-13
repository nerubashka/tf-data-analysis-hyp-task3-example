import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import boxcox

chat_id = 460109099 # Ваш chat ID, не меняйте название переменной
alpha = 0.06

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    X, Lambda = boxcox(x)
    _, p_value = ttest_ind(X, boxcox(y, lmbda=Lambda), alternative="greater")
    return p_value < alpha # Ваш ответ, True или False
