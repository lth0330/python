# 예외처리 : 예외가 발생할 상황을 예측하고 모두 조건문으로 처리하는 것은 매우 힘들다. 
# 예외가 발생하면 프로그램이 강제로 종료되지 않게 흐름제어 하기  = 예외처리 
# try : ~ except : ~

try :
   a = int (input("정수입력 : "))

except :
   # 만약에 예외가 발생했을 때 코드
   print("정수만 입력하세요 ")

# pass : 예외처리가 아닌 일단 생략할 경우 
la = [ "52","273","32","스파이", "103"]

list_a = []

for item in la :
   try :
    float(item)  # float() 실수타입으로 변환 함수
    list_a.append(item)
   except :
      pass       # 예외 발생시 아무것도 하지 않고 일단 통과 

print(list_a)


# else : 예외가 발생하지 않았을 때 코드 

try :
   a = int (input("정수입력 : "))

except :
   # 만약에 예외가 발생했을 때 코드
   print("정수만 입력하세요 ")

else :
   print("예외가 발생하지 않았을때 실행할 코드 ")


# finally : 무조건 실행할 코드
try :
   a = int (input("정수입력 : "))

except :
   # 만약에 예외가 발생했을 때 코드
   print("정수만 입력하세요 ")

else :
   print("예외가 발생하지 않았을때 실행할 코드 ")

finally : 
  print("프로그램 종료")


a = 10 ,"개"
a
