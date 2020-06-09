import pandas as pd

obj = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(obj)

print(obj['c'])
print(obj[['d', 'a']])
print(obj[1:4])