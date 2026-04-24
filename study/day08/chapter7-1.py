# OS 모듈
import os               # OS 모듈 호출 
print( os.name )        # nt : 윈도우 뜻
print( os.getcwd() )    # 현재 최상위 폴더 
print( os.listdir() )   # 현재 최상위 폴더의 내부 요소
os.mkdir('hello')       # 폴더 생성 
os.rmdir('hello')       # 폴더 삭제 
with open( 'study/day08/original.txt' , 'w') as file :
    file.write( 'hello')
os.rename( 'study/day08/original.txt' , 'study/day08/new.txt' )     # 파일명 변경 
os.remove( 'study/day08/new.txt' )  # 파일 삭제 
os.system( 'dir' )      # 시스템 명령어 실행    # 보안 문제 주의!

# dateitem 모듈 
import datetime
print( datetime.datetime.now() )        # 2026-04-24 09:55:22.829533
now = datetime.datetime.now()
print( now.year )                       # 2026
print( now.month )                      # 4
print( now.day )                        # 24
print( now.hour )                       # 9
print( now.minute )                     # 57
print( now.second )                     # 21
# 형식 : Y 년 m 월 d일 H시 M분 S초
output_a = now.strftime( '%Y-%m-%d %H:%M:%S')  # 형식만들기 
print( output_a )
# 시간 계산 
output = now.replace( year=( now.year + 1 ) , month=( now.month -1 ) )
print( output )

# item 모듈 
import time
print( '3초간 일시정지' )
time.sleep( 3 )         # 3초간 일시정지    # 스레드 일시정지 , 스레드란? 코드가 실행되는 흐름단위
print( '땡')

# urllib 모듈 
from urllib import request  # from 이용하여 특정한 함수/변수 만 가져오기

target = request.urlopen( "https://google.com" )
output = target.read()

print( output )




