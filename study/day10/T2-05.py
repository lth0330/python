import numpy as np
# 병합 , .concatenate( (x ,y) , axis = 0 )   , axis = 0(행기준) 1(열기준)
x = np.array( [ [1,2] , [3,4] ] )
y = np.array( [ [5,6] , [7,8] ] )
print( np.concatenate( (x, y) , axis= 0 ) ) # x 아래 로 y가 붙인다.
print( np.concatenate( (x, y) , axis= 1 ) ) # x 오른쪽으로 y가 붙인다.

# 정렬 , .sort( x ) : 오름차순정렬 ,  .sort( x )[ : : -1 ] : 내림차순정렬
x = np.array( [ 3, 1, 2, 5, 4 ] )
print( np.sort( x ) )               # [1 2 3 4 5]
print( np.sort( x )[ : : -1] )      # [5 4 3 2 1]

# 2차원 정렬  , .sort( x , axios = 0 ) , axis = 0(열기준) 1(행기준) None( 1차원 정렬 )
x = np.array( [ [12, 1, 2 ] , [9, 8, 7 ] ] )
print( np.sort( x , axis= 0 ) ) # 열 기준 오름차순 
print( np.sort( x , axis= 1 ) ) # 행 기준 오름차순 
print( np.sort( x , axis= None ) ) # [ 1  2  7  8  9 12] # 1차원 평탄화후 정렬
# 2차원 정렬 내림차순 주의할점 : 2차원 슬라이싱 사용 , [ 행슬라이싱 , 열슬라이싱 ] 
print( np.sort( x , axis = 0)[ :: -1 , : ] )    # 열 기준 내림차순 
print( np.sort( x , axis = 1)[ : , :: -1 ] )    # 행 기준 내림차순 

# np.sort( x ) 복사본반환  vs  배열.sort( x ) 원본수정    , 차이점 존재한다. 
x = np.array( [5,1,3] )
print( np.sort( x ) ) 
print( x.sort() )
print( x )

# .lexsort( 2차기준 , 1차기준) , 다중 정렬 , 1차 정렬후 만약에 1차정렬에서 동일한 값이 존재하면 동일한 값끼리 2차정렬 
x = np.array( [25, 30, 22, 24 ] )   # 1차원리스트
y = np.array( ['철수' , '영희' , '민수' , '영희'] ) #1차원리스트 
z = np.lexsort( ( x, y ) ) 
print( y[z] )   # y 먼저 정렬 후
print( x[z] )   # y 정렬 후 동일한 값끼리 2차 정렬

# 필터링 
x = np.array( [10,20,30,40,50] )
print( x > 30 )         # [False False False  True  True]
print( x[ x > 30 ] )    # [40 50]

y = np.array( [ [1,2,3] , [4,5,6] , [7,8,9] ] )
print( y % 2 == 0 )
print( y[ y%2==0 ] )    # [2 4 6 8]

# 조건부 필터링 , .where( 조건 , 참 , 거짓 ) 
print( np.where( x > 30 , x , 0 ) )    # 만약에 요소값이 30보다 크면 그대로 , 아니면 0
print( np.where( y%2==0 , y , 1 ) )    # 만약에 요소값이 짝수 이면 그대로 , 아니면 1

# 마스크 필터링 , 마스크(가리다) 조건식에 Flase 만 사용. , .ma.array( x , mask = 조건식 )
con1 = x > 30   # 30 초과 마스크(가린다.)
print( con1 )   # [False False False  True  True]
z = np.ma.array( x , mask= con1 )   # ma( 마스크 배열 : masked Array)
print( np.ma.sum( z ) )

# 다수 조건 필터링 
con2 = y % 2 == 0   # 조건1 : 짝수 
con3 = y % 4 == 0   # 조건2 : 4배수 

print( y[con2 & con3] )  # 비트 연산자. # [4 8] # 모든 조건을 충족하면 
print( y[con2 | con3] )  # [2 4 6 8] # 하나 조건을 충족하면 
print( y[~con2] )        # [1 3 5 7 9] # 조건에 부정 , 짝수->홀수 

# 특정 조건 충족하는 배열 반환 , .extract( 조건 , x ) : 조건을 충족하는 요소만 추출 
print( np.extract( y % 2 == 0  , y ) )  # [2 4 6 8]