
### 1.1 Two types of errors in the test

![The-confusion-matrix-of-accepting-or-rejecting-the-null-hypothesis-H0-or-the png](https://user-images.githubusercontent.com/54937248/71641025-6eb2ef80-2cd8-11ea-988f-0b7afe758802.jpeg)

###  Table 1.2 Probability of error β of the second kind and power 1-β (P.5)

```python
import numpy as np
import pandas as pd
def  a_test():
      return P ** 6 + (1-P) **6 
P = np.array ([0, 0.05, 0.10, 0.20, 0.30, 0.40 , 0.50, 0.60 , 0.70, 0.80 , 0.90, 0.95, 1.00])
x = [1]
B = y = x - a_test()
df= pd.DataFrame({"P":P,
                  "B":B} ,)
df["1-B"] = 1 - B
df

# 
"""
result
	P	B	1-B
0	0.00	0.000000	1.000000
1	0.05	0.264908	0.735092
2	0.10	0.468558	0.531442
3	0.20	0.737792	0.262208
4	0.30	0.881622	0.118378
5	0.40	0.949248	0.050752
6	0.50	0.968750	0.031250
7	0.60	0.949248	0.050752
8	0.70	0.881622	0.118378
9	0.80	0.737792	0.262208
10	0.90	0.468558	0.531442
11	0.95	0.264908	0.735092
12	1.00	0.000000	1.000000
"""
```


###  Picture 1.1 Probability of error β of the second kind and power 1-β (P.10)

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.special import comb
from scipy import stats
import scipy.stats as st

fig, ax = plt.subplots()


# 6回、９回の試行
n1 = 6
n2 = 6
n3 = 9

# 表が出る確率(帰無仮説)
x1=x2=x3=x = np.array ([0, 0.05, 0.10, 0.20, 0.30, 0.40 , 0.50, 0.60 , 0.70, 0.80 , 0.90, 0.95, 1.00])

# 1-β
y1= []
y2 = []
y3 = []
for i in x:
      a1 = stats.binom_test(0, n1, i, alternative='less') # x = 0の場合
      a2 = stats.binom_test(6, n1, i, alternative='greater')# x =6 の場合
      a3 = stats.binom_test(1, n2, i, alternative='less') # x <= 1 の場合
      a4 = stats.binom_test(5, n2, i, alternative='greater')# x >=5 の場合
      a5 = stats.binom_test(1, n3, i, alternative='less') # x <=1の場合
      a6 = stats.binom_test(8, n3, i, alternative='greater')# x >=8 の場合
      y1.append(a1+a2)
      y2.append(a3+a4)
      y3.append(a5+a6)


c1,c2,c3= "blue","green","red"      # 各プロットの色
l1,l2,l3= "ex1.7","ex1.8","ex1.9" # 各ラベル



ax.set_title(r'$Power curve$') # グラフタイトル
plt.gca().set_aspect('equal', adjustable='box')  # 方眼紙テクニック
ax.set_xlabel('x')  # 横軸のラベル
ax.set_ylabel('y',  rotation=0)  # 縦軸のラベル
ax.grid()  # グリッド（目盛り線）を表示
ax.plot(x1,y1, color = c1 ,label =l1)
ax.plot(x2,y2, color = c2 ,label =l2)
ax.plot(x3,y3, color = c3 ,label =l3)
ax.legend(loc=0)    # 凡例
plt.figure(figsize=(50,50),dpi=2000)  # レイアウトの設定
# plt.savefig('hoge.png') # 画像の保存
plt.show()

#result
```
![Unknown](https://user-images.githubusercontent.com/54937248/71776010-fe081d80-2fcc-11ea-99cc-5e223cde2592.png)

