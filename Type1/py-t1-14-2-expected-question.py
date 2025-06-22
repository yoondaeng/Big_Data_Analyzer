# %% [code]
# city와 f4를 기준으로 f5의 평균값을 구한 다음, f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)
# - 데이터셋 : basic1.csv 
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - File -> Editor Type -> Script


import pandas as pd

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df.head()
# df.info()
# print(df.shape)

# print(help(df.groupby))
# groupby 사용 후 계층적 인덱스(MultiIndex)를 가진 DataFrame
#                f5
# city  f4          
# 서울    A     123.4
# 서울    B     234.5
# 부산    A     345.6
# ...         


df = df.groupby(['city', 'f4'])[['f5']].mean()
print(df)

# print(dir(df))
# print(help(df.sort_values))
# print(help(df.reset_index))


# 일반 컬럼으로 복원
#    city f4      f5
# 0   서울  A  123.4
# 1   서울  B  234.5
# 2   부산  A  345.6
# ...


df = df.reset_index().sort_values('f5', ascending=False).head(7)
print(df)


print(round(df['f5'].sum(), 2))

#결과값 : 643.68