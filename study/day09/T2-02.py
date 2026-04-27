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

# [3] 배열의 데이터 타입

# .array(자료, dtype= numpy.타입명)
x = np.array([1,2,3], dtype=np.int64)
print(x.dtype)

# 필요에 따라 적절하게 bit 선택한다.
x = np.array([1.0,2.0,3.0], dtype=np.float64)
print(x.dtype)

x = np.array([True, False, True], dtype=np.bool_)
print(x.dtype)  # bool , 논리형

x = np.array(["apple","banana","cherry"], dtype=np.bytes_)
print(x.dtype)   # 문자열을 바이트형태로 저장 

# astype(numpy.변환할 타입명) , 타입변환
x = np.array([1.5,3.3,4.7])  # 실수
print(x.dtype)
y = x.astype(np.int32)  # float64 -> int32
print(y)   # [1 3 4] , int(정수형)은 소수점을 표현할 수 없으므로 소수점 잘림.
