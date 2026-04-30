
import numpy as np

data = np.genfromtxt(
    './layoffs_events.csv',
    delimiter=',',
    encoding='utf-8',
    skip_header=1,
    dtype=str,
    invalid_raise=False # 불러오기 실패한 행은 제외
    
)
print(data.shape)

# 1. 5열에서 공백이면 제외하자.

print( data[ data[ : , 4 ] != '' ].shape ) 
공백제거된5열 = data[ data[ : , 4 ] != '' ]

print( 공백제거된5열[ 공백제거된5열[ : , 2 ] == '' ].shape ) 
data = 공백제거된5열[ 공백제거된5열[ : , 2 ] != '' ]

rate = data[ : , 4 ] 
r = np.char.replace(rate, '%', '')
pct_workforce = r.astype(int)


# np.sum(pct_workforce)
# b = np.sum(pct_workforce)


layoff = data[ : , 2]
실업자 = layoff.astype( float )
layoff_count = 실업자.astype(int)

total_layoff = np.sum(layoff_count)


empl = layoff_count* (100/ pct_workforce)
emp = empl.astype(int)
print(emp)   # 중간에 말도 안되는 값이 들어가 있음
emp = emp[emp>0]
total_emp= np.sum(emp)

result = (total_layoff / total_emp)* 100
print(result,"%")  # 전체 평균 실업률 






# total_sum = (100/b)*a

# rate = data[ : , 4 ] 
# r = np.char.replace(rate, '%', '')
# 비율 = np.where(r == "" , "0", r)

# 실업률 = 비율.astype(int)
# pct_workforce = 실업률[실업률 >1]

# 해고열 = data[ : , 2]
# 조건 = np.where( 해고열 == '' , '0' , 해고열 )
# 타입조건 = 조건.astype( float )
# layoff_count = 타입조건[타입조건 > 1]

# total_sum = (100/pct_workforce)*layoff_count

# print( '전체직원수 : ' , total_sum )
# # 
# x = np.where( np.isinf(total_sum) , 0 , total_sum ) 
# print( x > 1 )
# y = 타입조건 / x

# # y = np.nan_to_num( y[~np.isinf(y)] , copy=False)


