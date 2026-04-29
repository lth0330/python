import numpy as np

# 1차원 배열 통계 
x = np.array([4,8,3,9,5])

print(np.min(x))    # 최소값
print(np.max(x))    # 최대값
print(np.argmin(x)) # 최소값(인덱스) 위치
print(np.argmax(x)) # 최대값(인덱스)위치
print(np.ptp(x))    # 최대값 - 최소값
print(np.sum(x))    # 합계



# 사분 위수 , 구역을 4개 구역으로 나눠서 데이터 분포 위치 파악 , q1 : 제1사분위수, 
q1 = np.percentile(x , 25)   # 1/4 , 25%   하위 25%
q3 = np.percentile(x , 75)   # 3/4 , 75%   하위 75% (상위 25%)
print(q1)
print(q3)
q2 = np.percentile(x, 50)    # 2/4 , 50%   중앙값
print(q2)

q4 = q3 - q1
print(q4)

# 2차원 배열 통계  ,  통계 함수( x, axis = 0)  0 = 열기준  1 = 행기준
y = np.array([[1,2,3],[4,0,6]])
print(np.min(y))
print(np.min(y, axis = 0))   # 열개수가 3개니까 최소값 3개
print(np.min(y, axis = 1))   # 행개수가 2개니까 최소값 2개
print(np.max(y))             # axis 생략하면 2차원배열 평탄화 (1차원으로변경)해서 통개 구함
print(np.argmax(y))          # 최대값 위치
print(np.argmin(y))          # 최소값 위치
print(np.sum(y))
print(np.mean(y))