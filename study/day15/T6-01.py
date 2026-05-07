# T6-01
import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  # 


#[1. 타이타닉 생존 데이터 분석]
#출처: Kaggle - Titanic: Machine Learning from Disaster
#https://www.kaggle.com/competitions/titanic/overview

df = pd.read_csv('study/day15/train.csv',       # 파일 경로
                 header=0,                 # 시작할 행번호(0부터 시작)
                 encoding='utf-8',          # 인코딩(한글 : utf-8 , cp949, euc-kr) , 파일마다 다를 수 있다.
                                   )   
print(df.head())
df.info()

#[2. 가설]
#가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 원칙)
#가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
#가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

#[3. 데이터 전처리]
#수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
#범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.

# 나이 : 중앙값 , 승선 항구 : 최빈값
df['Age'] = df['Age'].fillna( df['Age'].median() )
df['Embarked'] = df['Embarked'].fillna( df['Embarked'].mode()[0])
print(df.isnull().sum())

#[3. 데이터 시각화 및 분석]
#3-1 : sns.countplot을 사용하여 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
sns.countplot(df, x='Survived').set_xticklabels(['사망','생존'])
# plt.xticks([0,1],['사망','생존'])  # 범주형 x축 레이블 수정 
plt.title('생존 여부')
plt.show()
#3-2 : sns.histplot을 사용하여 연령대별 상세 분석:나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
print(df[df['Survived']== 0]['Age'])    # 사망한 사람의 나이
print(df[df['Survived']== 1]['Age'])    # 생존한 사람의 나이
sns.histplot(df[df['Survived']== 0]['Age'],label='사망',color="#ff0000", kde=True)
sns.histplot(df[df['Survived']== 1]['Age'],label='생존',color="#000dff", kde=True)

plt.title('나이에 따른 생존분포')
plt.xlabel('나이')
plt.ylabel('생존/사망')
plt.legend()
plt.show()
#3-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.

sns.countplot(data=df, x='Sex',hue='Survived') # 생존자 수

plt.xlabel('성별')
plt.ylabel('생존자')
plt.show()

#3-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.

sns.countplot(data=df, x='Pclass',hue='Survived') # 생존자 수
plt.xlabel('객실 등급')
plt.ylabel('생존자')
plt.show()

#3-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.

sns.countplot(data=df, x='Survived',hue='Survived') # 생존자 수
plt.legend()
plt.xlabel('승선 항구')
plt.ylabel('생존자')
plt.show()





