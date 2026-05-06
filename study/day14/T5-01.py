
# T5 - 01/py
import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도

# [1] JSON 파일에서 특정한 열 ("customer_data")만 가져와서 데이트프레임 구성
with open('study/day14/T5_data.json','r',encoding='utf-8') as json_file :
    data_json = json.load(json_file)
    df_customer = pd.DataFrame(data_json['customer_data'])
    print(df_customer.head())

# [2] 데이터 분석 / 시각화
# (1) 성별과 연령대로 그룹화 , df.groupby( ['그룹기준',그룹기준])
# (2) 통계 df.agg( {'열이름',: '함수명'})
# (3) 여러개 그룹화할 경우에는 .reset_index() 함수를 이용하여 행번호를 붙인다.
newDf = df_customer.groupby(['성별','연령대']).agg({'고객 수':'sum','평균 구매 금액':'mean'})
print(newDf)                         # 성별 + 연령대 별 총고객수(합계) 와 평균 구매금액의 평균
print(newDf['연령대'])                # 남성 여성 포함하여 중복된 연령대
print(newDf['연령대'].unique())       # 남성 여성 포함하여 중복 제거된 연령대
# 1. 연령대별(그룹) 총 고객수 막대그래프 
# (1) plt.bar(x축값 , y축값)
# plt.bar(newDf['연령대'], newDf.groupby(['연령대'].agg({'고객수':'sum'})['고객 수']),color = 'blue' )

# 2. 성별 + 연령대별(그룹) 막대그래프 생성


# 3. 연령대별(그룹) '평균 구매 금액' 가로 막대그래프 