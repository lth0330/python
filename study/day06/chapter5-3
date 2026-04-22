
# 콜백함수 : 함수의 매개변수에 사용하는 함수 

def call_10_items(func) :  # 매개변수로 받은 함수  
  for i in range(10) :
    func()

def print_hello ():
  print("안녕하세요")

call_10_items(print_hello)  # 함수 그자체 
# call_10_items(print_hello())  # 함수 실행  # 예외발생

# map(), filter() 함수
# map( 함수, 리스트 ) : 리스트의 요소를 하나씩 함수매개변수에 대입하여 새로운리스트 반환
# filter ( 함수, 리스트 ) : 리스트의 요소를 하나씩 함수매개변수에 대입하여  참(True)인 경우 새로운리스트 반환

def power( item ) :
  return item * item

def under_3(item) :
  return item < 3

list_input_a = [ 1, 2, 3, 4, 5] #  

output_a = map(power , list_input_a)
print(list(output_a))

output_b = filter(power, list_input_a)
print(list(output_b))

# 제너레이터 : 함수 내부에 yield 키워드를 사용하여 next()함수를 외부에서 호출하여 yield 키워드까지 실행한다
def test() :
  print("A 지점 통과")
  yield 1
  print("B 지점 통과")
  yield 2

test()            # 함수 호출시 실행이 안된다.
output = test()  

a=next(output)
print(a)
b=next(output)
print(b)


# 람다 : 함수 선언 간단하게 하는 문법
# lambda 매개변수 : 반환값

# 방법 1
power = lambda x : x*x
output_a = map(power , list_input_a)
print(output_a)

# 방법 2 
output_a = map(lambda x : x*x ,list_input_a)
print(output_b)


# 파일 처리
# open( 파일경로 , 읽기 모드)
# 읽기모드 : W - 새로쓰기 , a - 이어쓰기 , r - 읽기 모드

# (1) open 함수를 이용하여 지정한 경로에 파일 쓰기
file = open('study/day06/basic.txt', 'w')  # 현재 파이썬 파일 폴더내 basic.txt 생성 

# (2) .write(출력할 내용 ) 함수 이용한 내보내기
file.write("I want to go home")

# (3) .close() 함수 이용한 안전하게 스트림 닫기
file.close

# (4) 
with open("study/day06/basic2.txt", "w") as file :
  file.write("안녕 파이썬 프로그래밍2..!")

# 스트림이란? 데이터가 흐르는 길 , 바이트단위 , 프로그래밍 언어가 외부 자료와 연결 (파일, JDBC, 네트워크)

# (5)  .read() 함수를 이용한 파일 읽어오기
with open("study/day06/basic.txt", "r") as file :
  contents = file.read()
print(contents)



# 랜덤하게 1000명의 키와 몸무게 만들기
import random

한글 = list("가나다라마바사아자차카타파하")

with open("study/day06/info.txt","w") as file :
  for i in range(1000):
    name = random.choice(한글) + random.choice(한글) + random.choice(한글)
    weight = random.randrange(40, 100)
    height = random.randrange(150,190)
    
    file.write("{},{},{} \n".format(name, weight, height))



# 반복문으로 파일 한줄씩 읽기 
with open("study/day06/info.txt","r") as file :
  for line in file :
    (name, weight, height) = line.strip().split(",")

    if ( not name) or (not weight) or (not height) :
      continue

    bmi = int(weight) / ((int(height) / 100) ** 2)
    result = ""
    if 25 <= bmi :
      result = "과체중"
    elif 18.5 <= bmi :
      result = "정상체중"
    else :
      result = "저체중"
    
    print( "\n".join([
      "이름 : {}",
      "몸무게 : {}",
      "키 : {}",
      "BMI : {}",
      "결과 : {}"
    ]).format(name,weight,height,bmi,result))
    print()
    