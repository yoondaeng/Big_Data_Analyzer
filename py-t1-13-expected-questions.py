# %% [code]
# %% [code]
# 상관관계 구하기
# 주어진 데이터에서 상관관계를 구하고, quality와의 상관관계가 가장 큰 값과, 가장 작은 값을 구한 다음 더하시오!
# 단, quality와 quality 상관관계 제외, 소수점 둘째 자리까지 반올림하여 계산

# - 데이터셋 : ../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - 스크립트 방식 권장: File -> Editor Type -> Script

# import pandas as pd
# import numpy as np

# df = pd.read_csv('/kaggle/input/red-wine-quality-cortez-et-al-2009/winequality-red.csv')
# print(df.head())
# print(df.shape)

# df_corr = df.corr()
# df_corr = df_corr[:-1] # quality와 quality 상관관계 제외
# # print(df_corr['quality'])

# max_corr = abs(df.corr()['quality'][:-1]).max()
# min_corr = abs(df.corr()['quality'][:-1]).min()

# if max_corr not in df.corr()[['quality']][:-1].values:
#     max_corr = -max_corr
# if min_corr not in df.corr()[['quality']][:-1].values:
#     min_corr = -min_corr

# ans = round(max_corr + min_corr, 2)
# print(ans) # 0.49

import pandas as pd

# 데이터 불러오기
df = pd.read_csv('/kaggle/input/red-wine-quality-cortez-et-al-2009/winequality-red.csv')

# quality와 다른 변수 간의 상관관계 Series 만들기 (자기자신 제외)
# df.corr()은 대칭 행렬 (correlation matrix)을 반환
corr_series = df.corr()['quality'].drop('quality')

# 최대, 최소 상관계수 구하기 (절댓값 기준)
max_corr = corr_series.abs().max()
min_corr = corr_series.abs().min()

# 정답: 두 값을 더해서 소수점 둘째 자리까지 반올림
ans = round(max_corr + min_corr, 2)
print(ans)
