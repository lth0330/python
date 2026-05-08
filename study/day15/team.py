import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  # 

df = pd.read_csv('study/day15/train_HousePrices.csv',       # 파일 경로
                 header=0,                 # 시작할 행번호(0부터 시작)
                 encoding='utf-8',          # 인코딩(한글 : utf-8 , cp949, euc-kr) , 파일마다 다를 수 있다.
                                   )   
print(df.head())


# 'LotFrontage', 'MasVnrArea', 'GarageYrBlt' 등의 수치형 변수의 결측치는 데이터의 중앙값(Median)으로 대체하여 보정한다.
df['LotFrontage'] = df['LotFrontage'].fillna( df['LotFrontage'].median() )
df['MasVnrArea'] = df['MasVnrArea'].fillna( df['MasVnrArea'].median() )
df['GarageYrBlt'] = df['GarageYrBlt'].fillna( df['GarageYrBlt'].median() )

# 정보 부재가 명확한 범주형 변수('Alley', 'PoolQC', 'Fence' 등)는 결측치를 'NoAlley', 'NoPool', 'NoFence'와 같이 특정 문자열로 대체한다.
df['Alley'] = df['Alley'].fillna('NoAlley')
df['PoolQC'] = df['PoolQC'].fillna('NoPool')
df['Fence'] = df['Fence'].fillna('NoFence')
df['MiscFeature'] = df['MiscFeature'].fillna('NoMisc')


print(df.isnull().sum())


# 아래 17개 주요 범주형 변수는 최빈값(Mode)을 활용하여 결측치를 일괄 보정한다.
fill_list = [
    "BsmtQual",
    "BsmtCond",
    "BsmtExposure",
    "BsmtFinType1",
    "BsmtFinType2",
    "Electrical",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "GarageQual",
    "GarageCond",
    "MSZoning",
    "Functional",
    "SaleType",
    "Exterior1st",
    "Exterior2nd",
    "MasVnrType"
    ]
for i in fill_list:
    df[i] = df[i].fillna(df[i].mode()[0])
df.info()

# 가설2 : 주택의 스타일 (HouseStyle)이나 외장재 (Exterior1st)에 따라 가격 분포의 차이가 뚜렷할 것이다.

# 5-3. 주택 스타일별 가격 분포 비교 (가설 2 검증)
# sns.boxplot을 사용하여 주택 스타일(HouseStyle)별 가격 분포와 이상치(Outlier)를 파악한다.

sns.boxplot( data=df ,gap=0.5 ,x='HouseStyle',y='SalePrice')
plt.title('주택 스타일별 가격 분포')
plt.xlabel('주택스타일')
plt.ylabel('가격')

plt.show()

# 5-4. 주요 외관 요소별 가격 분포 비교 (가설 2 검증)
# sns.boxplot을 사용하여 지붕 스타일(RoofStyle) 및 외장재(Exterior1st)에 따른 가격 차이를 분석한다.


sns.boxplot( data=df ,gap=0.5 ,x='Exterior1st',y='SalePrice')

print((df[df['Exterior1st']=='CBlock']['SalePrice']).max())
print((df[df['Exterior1st']=='CBlock']['SalePrice']).min())
plt.title('주택 스타일별 가격 분포')
plt.xlabel('지붕 스타일 및 외장재')
plt.ylabel('가격')
plt.show()