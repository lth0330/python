
# T2-01.py
# numpy 이란?  고성능 수치 계산 라이브러리
# 설치 : 터미널에서 " pip install numpy"
# numpy 불러오기 : import numpy

import numpy
print(numpy.__version__)

# [1] 넘파이 배열 생성
x = [1,2,3,4] # 일반 리스트
print( x )    # [1,2,3,4]

x = numpy.array([1,2,3,4])
print(x)

x = numpy.array([[1,2,3],[4,5,6]])
print(x)

x = numpy.zeros((3,2))  #.zeros((행,열))   행 과 열 만큼의 0으로 초기화
print(x)

x = numpy.ones((2,3))
print(x)

x = numpy.full((2,4),10)
print(x)

# .arange(시작,끝, 단위) , 시작부터 끝 사이의 단위로 구성된 배열
x = numpy.arange(0,10,3)
print(x)

# .linsoace (시작, 단위, 차이)  
x = numpy.linspace(0,10,5)   # 0부터 10까지 5로 나눠줌 
print(x) #[0 2 4 6 8]
 
