# %% [code]
# 주어진 데이터에서 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균을 구하고, 그 차이를 구해보세요 
# (단, 100%가 넘는 접종률 제거, 소수 첫째자리까지 출력)

# - 데이터셋 : ../input/covid-vaccination-vs-death/covid-vaccination-vs-death_ratio.csv
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - File -> Editor Type -> Script


import pandas as pd

df = pd.read_csv("/kaggle/input/covid-vaccination-vs-death/covid-vaccination-vs-death_ratio.csv")
print(df.head())
print(df.shape)

df2 = df.groupby('country').max()
df2 = df2.sort_values(by='ratio', ascending = False)

print(df2)

# 100% 넘는 접종률 제거
cond = df2['ratio'] <= 100
df2 = df2[cond]
print(df2.shape) # 194

# 상위 10개의 평균
top = df2['ratio'].head(10).mean()
# top = df2['ratio'][:10].mean()
print(top)

# 하위 10개의 평균
bottom = df2['ratio'].tail(10).mean()
# bottom = df2['ratio'][194:183:-1].mean()
print(bottom)

print(round(top - bottom, 2)) # 88.37

