# T5-04.py
import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도

# [1] T5_data.json 파일 내 'risk_return_data'
with open('study/day14/T5_data.json','r',encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['risk_return_data'])
print(df)

# [2] 산점도 : 리스트 대비 수익률
plt.scatter(df['리스크'],df['수익률(%)'],s=df['수익률(%)']*20,alpha=0.3)
plt.title('리스크 대비 수익률')
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.show()



# [3] 산점도 : 자산별(글부) 리스크 대비 수익률 
categories = df['자산'].unique()  # 중복 제거된 자산 리스트 
print(categories)
for i , category in enumerate(categories) :   # enumerate(리스트) 반복순회자로 인덱스와 요소값 하나씩 반환  
    sub = df[df['자산']==category]  # 동일한 자산 접오 가져오기.
    print(sub)
    plt.scatter(sub['리스크'],sub['수익률(%)'], label = category)
plt.legend()
plt.show()

