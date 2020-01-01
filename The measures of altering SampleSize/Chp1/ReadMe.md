
### 1.1 Two types of errors in the test

![The-confusion-matrix-of-accepting-or-rejecting-the-null-hypothesis-H0-or-the png](https://user-images.githubusercontent.com/54937248/71641025-6eb2ef80-2cd8-11ea-988f-0b7afe758802.jpeg)

### 1.2 Probability of error β of the second kind and power 1-β

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

```
