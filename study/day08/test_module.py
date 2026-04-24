# 변수 
PI = 3.141592
# 함수1 
def number_input() :
    output = input( '숫자 입력>' )
    return float( output )
# 함수2 
def get_circumference( radius ) :
    return 2 * PI * radius
# 함수3
def get_circle_area( radius ) :
    return PI * radius * radius 

# **프로그램 진입점** 
if __name__ == "__main__" :
    print( "프로그램 진입점 ")
    print( get_circumference(10) )
    print( get_circle_area(10) )