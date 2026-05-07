
# T5-05
import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns
# [1] T5_data.json 파일 내 'financial_performance_data'
with open('study/day14/T5_data.json','r',encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['financial_performance_data'])
print(df)
# [2] 플롯박스 : '수익' '비용' '이익' 으로 박스플롯 표시   
# plt.boxplot() : 데이터최솟값, 최대값, 1사분위, 중앙값 3사분위 시각화
plt.boxplot([df['수익'],df['비용'],df['이익']], tick_labels=['수익','비용','이익'])
plt.title('항목별 금액 분포(플롯박스)')
plt.show()

# 차트 확인 : 비용 데이터에서 800 부근에 이상치가 존재한다. 

# [3] 플롯박스 :분기별 수익 데이터로 박스플롯 표시 
# 플롯박스에서 그룹 , df.boxplot(column=['값'],by='그룹기준)
df.boxplot(column = ['수익'], by='분기')
plt.show()

#