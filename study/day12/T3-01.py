# numpy : 배열 기반( 위치(인덱스) ) , 공학 수치 계산
# pandas : 테이블 기반( 라벨(인덱스) ) , 전처리/필터링(+numpy)
    # 1차원 : series        # 2차원 : dataframe

# [1] pandas 설치 : pip install pandas
# [2] import pandas as pd

import pandas as pd
print( pd.__version__ ) # 3.0.2

# series 
# 1. 생성 
x = [ 10 , 20 , 30 , 40 ]  # 리스트 
z = pd.Series( x )
print( z ) 
# 0    10           # 0 ~ 4 : 각 요소들의 인덱스
# 1    20           # 10~50 : 각 요소의 값 
# 2    30
# ~~~~~
# dtype: int64      # 데이터의 타입 

# 2. 각 요소들의 라벨 포함하기 
y = [ 'a' , 'b' , 'c' , 'd' ]
z = pd.Series( x , index=y )    # index에 라벨(목록) 대입 
print( z )
# a    10           # a ~ d : 각 요소들의 인덱스(라벨)
# b    20          
# c    30
# dtype: int64

# 3. 딕셔너리 으로 생성 
# 파이썬 주요 타입 , [리스트] (튜플) {딕셔너리}
x = { 'apple' : 1 , 'banana' : 2 , 'cherry' : 3 }
z = pd.Series(  )
print( z )

# 4. 주요 속성 확인 
print( z.dtype )        # 타입반환 , int64
print( z.index )        # 인덱스반환, Index(['apple', 'banana', 'cherry'], dtype='str')
print( z.values )       # 값반환 , [1 2 3]
print( z.head(2) )      # .head(n) , 상위 n개(기본값:5) 개만 출력( 확인용 )
print( z.tail(2) )      # .tail(n) , 하위 n개 만 출력 

# 5. 인덱싱 , 슬라이싱 
print( z.iloc[0] )                      # iloc[인덱스번호] , 라벨이 아닌 위치로 조회
print( z.loc['apple'] )                 # loc[ 라벨명 ] , 라벨명으로 조회 
print( z.loc['apple' : 'cherry'] )      # loc[ 시작라벨 : 끝라벨 ]

# 6. 데이터 수정 
z['apple'] = 10             # [ 기존라벨명 ] = 새로운값 
print( z )
print( z['apple'] )         # [ 기존라벨명 ]

# 7. 데이터 추가 
z[ 'berry' ] = 40           # [ 새로운라벨명 ] = 새로운값 
print( z )

# 8. 병합 , .concat( [ x , y ] )
# 파이썬 리스트 합치기
x = [10,20,30]
y = [40,50]
print( x + y )          # [10, 20, 30, 40, 50]
print( [ x , y ] )      # [[10, 20, 30], [40, 50]]
print( [ *x , *y ] )    # [10, 20, 30, 40, 50]

# 판다스 합치기 , .concat( [ x , y ] )
x = pd.Series( [10,20,30] , index=['a','b','c'] )
y = pd.Series( [40,50] , index=[ 'd' , 'e' ] )
z = pd.concat( [ x , y ] )
print( z )

# 9. 라벨 이름 변경 , .rename( { '기존' : '새로운' } )
# 파이썬 , 문자(리터럴)
test = 'hello java'                 # hello java
test = test.replace( ' ' , '-')     # 문자열(리터럴)은 불변성 특징
print( test )                       # hello-java

x = z.rename( {'a' : 'apple' } )
print( x )

# 10. 필터링 , [ 조건식 ] , [ ( 조건식1 ) | ( 조건식2 ) ]
print( z[ z > 30 ] )            # 30초과 필터링 
x = z[ z > 30 ]
print( x )
x = z[ ( z < 25 ) | ( z > 35 ) ] #  25보다 작거나 35보다 크다 
print( x )
x = z[ ( z > 25 ) & ( z < 35 ) ] #  25보다 크면서 35보다 작다 
print( x )
z[ z > 30 ] = z[ z > 30 ] + 10  # 30초과 한 요소값에 10 더한 후 에 30 초과 한 요소에만 대입 
print( z )

# 11. 통계
print( z.sum() )            # .sum() 합계
print( z.mean() )           # .mean() 평균 
print( z.max() )            # .max() 최댓값 
print( z.min() )            # .min() 최솟값 
print( z.median() )         # .median() 중앙값 
print( z.var() )            # .var() 분산
print( z.std() )            # .std() 표준편차
print( z.count() )          # .count() 요소 개수 
print( z.value_counts( ) )   # 각 요소별 중복 개수
print( z.value_counts( normalize=True ) ) # 각 요소가 전체에서 차지하는 비율(0~1)

# 12. 정렬
x = z.sort_index()  # 인덱스(라벨) 기준의 정렬
print(x)

x = z.sort_values() # 값 기준의 정렬
print(x)

x = z.sort_index(ascending=False)  # 내림차순 정렬 (desc)
print(x)

x = z.sort_values(ascending=False)  # 내림차순 정렬 (desc)
print(x)

# 13. 그룹
print("13 그룹 ")

z = pd.Series([10,20,30,10,20,40],
              index=["a","b","a","b","a","b"])

x =z.groupby(level = 0).sum() # 인덱스(라벨)별 총합계
print(x)

x = z.groupby(level=0).mean() # 인덱스(라벨)별 평균
print(x)

x = z.groupby(level=0).agg(["sum","mean","count"])  # 여러개 집계합수는 agg 함수로 묶어서 사용 
print(x)



