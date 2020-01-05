import numpy as np
import pandas as pd
from scipy.special import comb
from scipy import stats
import scipy.stats as st
from decimal import Decimal, ROUND_HALF_UP



# 9回の試行
n = 9
# 表が出る確率(帰無仮説)
p = np.array ([0, 0.05, 0.10, 0.20, 0.30, 0.40 , 0.50, 0.60 , 0.70, 0.80 , 0.90, 0.95, 1.00])

b = np.array([1])

# 「反復試行の確率」の定理
xList=pd.Series([comb(float(n), x)*p**x*(1-p)**(float(n)-x) for x in range(0, n+1)])

# binom_testは両側確率で出てくるので1/2  , alternativeは片側検定("greater", "less") か両側検定("two-sided") 。
x = 0
y = []
for x in range(0,13):
      a1 = stats.binom_test(1, n, p[x], alternative='less') # x <= 1の場合
      a2 = stats.binom_test(8, n, p[x], alternative='greater')# x >= 8 の場合
      y.append(1-Decimal(a1+a2).quantize(Decimal(".00000"),rounding=ROUND_HALF_UP))

df= pd.DataFrame({"P":p,
                            "B": y} ,)
df["1-B"] = b- y
df
