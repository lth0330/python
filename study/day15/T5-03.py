# T5-03.py
import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도

# [1] T5_data.json 파일 내 'patient_status_data'
with open('study/day14/T5_data.json','r',encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['patient_status_data'])
print(df)

# [2] 막대차트 : 상태별 환자수 비교
# plt.bar(x축값, y축값)
plt.bar(df['상태'],df['환자 수'])
plt.title('상태별 환자 수 비교')
plt.xlabel('상태')
plt.ylabel('환자 수')
plt.show()

# [3] 원형차트 : 전체대비 각 상태의 환자 수 백분율
# plt.pie(값, labels=df['상태'],autopct='%비율%%',startangle= 시작각도)
plt.pie(df['환자 수'],labels=df['상태'],autopct='%.2f%%',startangle=90)
plt.title('환자 상태 비율')
plt.show()
