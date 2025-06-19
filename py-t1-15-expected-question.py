# %% [code]
# 주어진 데이터 셋에서 age컬럼 상위 20개의 데이터를 구한 다음 
# f1의 결측치를 중앙값으로 채운다.
# 그리고 f4가 ISFJ와 f5가 20 이상인 
# f1의 평균값을 출력하시오!

# - 데이터셋 : basic1.csv 
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - File -> Editor Type -> Script

import pandas as pd

# 데이터 불러오기
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

# print(help(df.sort_values)) 
df = df.sort_values('age', ascending=False)
df = df[:20]
print(df)

# print(df.isnull().sum())
df['f1'] = df['f1'].fillna(df['f1'].median())
# print(df.isnull().sum())

# f4가 ISFJ와 f5가 20 이상인
df = df[(df['f4'] == 'ISFJ') & (df['f5'] >= 20)]
# f1의 평균값을 출력하시오!
print(df['f1'].mean())
# 정답 : 73.875