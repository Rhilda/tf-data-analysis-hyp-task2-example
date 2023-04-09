import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    result = cramervonmises_2samp(x, y)
    p_value = result.pvalue
    alpha = 0.08
    return p_value < alpha
