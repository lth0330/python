# [2] 배열이 주요 속성
# .spape , 현재 배열의 크기 (튜플) 반환, (행개수, 열개수)

import numpy as np
x = np.array([[1,2,3,], [4,5,6]])
print(x.shape) # (2,3)

#.dtype, 현재 
x= np.array([1.0,2.0,3.0])
print(x.dtype)

# .size , 현재 배열내 모든 요소 수
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x.size) # 9

# .ndim , 현재 배열의 차원 수
x = np.array([1,2,3]) 
print(x.ndim)  # 1
x = np.array([[[1],[2]], [[3],[4]]])
print(x.ndim)  # 3

# .flat , 다차원 배열을 1차원으로 반환 
x = np.array([[1,2],[3,4], [7,5]])
for element in x.flat :
    print(element)