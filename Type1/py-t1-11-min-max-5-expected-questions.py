# %% [code]
# min-max스케일링 기준 상하위 5% 구하기
# 주어진 데이터에서 'f5'컬럼을 min-max 스케일 변환한 후, 상위 5%와 하위 5% 값의 합을 구하시오

# - 데이터셋 : basic1.csv
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - File -> Editor Type -> Script


# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")
print(df.head(5))
print(df.isnull().sum())

from sklearn.preprocessing import MinMaxScaler
# print(dir(sklearn.preprocessing))
scaler = MinMaxScaler()
df['f5_1'] = scaler.fit_transform(df[['f5']])

print(df.head())

lower = df['f5_1'].quantile(0.05)
print(lower)

upper = df['f5_1'].quantile(0.95)
print(upper)

print(lower + upper)