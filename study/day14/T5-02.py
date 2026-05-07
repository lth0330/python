# T5-02.py
import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도

with open('study/day14/T5_data.json','r',encoding= 'utf-8' ) as json_file :
    data_json = json.load(json_file)

    df_stock = pd.DataFrame(data_json['stock_data'])
    print(df_stock.head())

# 1. '기간'별 '주가'와 '평균 이동선(3개월)' 선 그래프 표현하고 '거래량'을 보조축(오른쪽 축) 막대그래프 표현 
# 1.fig(전체틀) , axs(축) = plt.subplots() : 한 화면에 여러개 차트 표현 사용 
fig , axs = plt.subplots()
# 2.  .plot( x축값, y축값)
axs.plot(df_stock['기간'], df_stock['주가'], label='주가', color = "#ffff00")

# 3. subblots() 사용시 라벨 작성 주의할점 : .xlabel --> set_xlabel 사용한다.
axs.set_xlabel('기간')
axs.set_ylabel('주가')

# 4. 선 추가 
axs.plot(df_stock['기간'], df_stock['평균 이동선(3개월)'], label='평균 이동선(3개월)', color = "#ff0000")

# 5. *** 보조축 : 오른쪽 세로축 *** , 기본축.twinx()
axs2 = axs.twinx()
axs2.bar(df_stock['기간'], df_stock['거래량'], label='거래량', color = "#000000", alpha=0.3)
axs2.set_ylabel('거래량')

# 6. 그래프 출력 
fig.suptitle('기간별 주가및 거래량 추세')   # 틀 제목 
plt.show()

# 차트 확인 : 1월 부터 12월까지 꾸준히 추세가 우상향 한다,
# 막대:비교 , 선:추세 , 히트맵(상관계수) : 변수간의 관계파악

# [2]. '주가','거래량','평균 이동선(3개월)' 간의 상관관계를 히트맵 표현  ( 상관계수 )
import seaborn as sns 
# 1. 자료들 간의 상관계수 표현 ,   .corr() , 자료들 간의 상관계수( -1 ~ +1 )를 자동으로 계산 
# df[ [열이름1 , 열이름2 , 열이름3] ].corr()
matrix = df_stock[ ['주가' , '거래량' , '평균 이동선(3개월)'] ].corr()
# 2. 상관계수를 히트맵으로 시각화
sns.heatmap( matrix , cmap='coolwarm' , annot=True , fmt='.2f' )
# 3. 
plt.title('변수들 간의 상관관계')
plt.show()

# 차트 확인 : 1에 가까우면 두 변수간의 상관관계가 크다. 주가와거래량의 상관계수는 0.99 이므로 강력한 선행지표,
# 즉] 주가가 증가하면 거래량도 증가한다


