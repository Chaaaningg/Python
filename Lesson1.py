import re
#function(함수)이란 무엇인가?
#함수란? : 특정한 기능을 수행하는 일련의 명령어들을 하나로 묶어서 이름을 붙인 것
#ex: print() : 출력하는넘 for() , while() : 반복하는넘
#함수를 사용하는 이유? : 반복적인 작업을 피하기 위해 + 코드의 가독성을 높이기위해? -> 효율적으로 할려고
#함수의 종류는 무엇이 있을까?
#크게 2가지
#내장함수 : 파이썬 , C , C++ , DotNet 등 기본적으로 제공하는 함수
#프로그램은 무엇인가?
#프로그램이란 : 여러가지 기능을 묶어 놓은 하나의 실행 파일
#파이썬 기존의 C , C++ , DotNet 등과 다르다
#왜냐?
#컴파일 과정이 없기 때문
#컴파일이란 무엇인가
#프로그레밍에서 컴파일이란
#기본개념!
#컴퓨터 : 어떤 방식의 언어를 알아들 수 있니?
#그렇지 컴퓨터는 binary (2진법) 으로만 작동한다
#그렇기에 우리가 쓰는 언어(자연어< human language) 영어든 한국말이든
#그걸 컴퓨터가 알아들을 수 있도로 binary로 바꿔줘야한다
#이때 컴파일러가 필요하다
#OR , AnD . Not , XOR , NAND , NOR , XNOR CPU는 이 게이트들 만으로 모든 연산을 수행할 수 있다
#그렇기 때문에 우리가 작성하는 프로그램 언어라는 것이 필요하고
#프로그램 언어가 하는 것은 번역해주는것이다
#그렇기에 문법이라는것이 있고
#컴파일러가 이 문법을 검사하여
#이것을 binary로 바꿔준다
#그렇기에 컴파일러가 필요하다
#컴파일 과정은 일단 우리가 지금 보는 이 랭귀지들
#MAIN , PRINT 이런걸
#단계적으로 번역해주는데
#1번째 SOURCE CODE -> 2번째 INTERMEDIATE CODE -> 3번째 MACHINE CODE
#왜냐?
#파이썬은 컴파일러가 없음
#그렇기에 인터프리터가 필요하다
#인터프리터란 무엇인가?
#인터프리터란 컴파일러와 다르게
#한줄씩 번역해서 실행하는 것
#컴파일러는 뭘하냐면
#파일 한꺼번에 읽어서
#변환후 컴터가 실행할수 잇는 바이너리 파일로 만듦
#인터프리터는
#걍 한줄씩 실행
#왜 컴파일러 없이 한줄씩 실행이 가능한가?
#파이썬은 내장으로 모든 신택스를 JIT (Just In Time)
#CPU 종류마다 명령어를 내리는 방식 다름 달라
#X86 , ARM , MIPS , RISC-V , SPARC , POWER
#ASSEMBLY LANGUAGE
#완전 바이너리는 아니더라도 컴터가 이해할수 있고 사람이 작성이 가능한
#가장 로우레벨 언어
#로우레벨은 무엇이냐?
#쉽게 얘기해서 cpu 에 일을 내리는데 가장 가까운 언어이기에 로우레벨이라 부른다
#근데 이게 존내게 어려움
#노가다 이런 노가다가 없음
#왜냐?
#메모리 ? 레지스터 ?
#컴퓨터는 메모리에 있는 데이터를 레지스터로 옮겨서 연산을 수행한다
#메모리에 값을 할당함
#할당한 값을 레지스터가 접근하여
#CPU에다가 일을 던짐
#그러면 CPU는 레지스터에 있는 값을 가지고
#연산을 수행함
#그러면 결과값을 레지스터에 저장함
#그러면 레지스터에 있는 값을 메모리에 저장함
#Variable(변수)이란 무엇인가?    
#그렇기에 존나 느림
#존내게 느려
    #메모리 할당방식
    #i 라는 변수를 선언하면
    #일단 메모리 주소를 잡아
    #그리고 그 주소에 값을 할당함
    #i 는 뭔지 모름 그냥 메모리 주소를 갖고있는거임
    #메모리 주소란 메모리에 있는 값을 찾아가는 주소
    #메모리 반도체 여러개 따닥따닥
    #그러면 그 반도체를 가리키는 이정표
    #i = integer 정수형
    #integer 는 정수형 변수이고
    #정수형 변수를 선언하는 순간
    #메모리에 정수형 변수를 위한 공간을 확보함
    #정수형 변수의 크기는
    #8바이트다
    #그러면 메모리에 8바이트 만큼의 공간을 확보함
    #그래서 정수형 변수 말고도
    #많은 변수들이 있음
    #정수형 변수는 정수를 저장하는 변수
    #실수형 변수는 실수를 저장하는 변수
    #문자형 변수는 문자를 저장하는 변수
    #문자열형 변수는 문자열을 저장하는 변수
    #불리언형 변수는 참과 거짓을 저장하는 변수
    #배열형 변수는 배열을 저장하는 변수
    #1 byte = 8 bit
    #1 bit = 0 or 1
    # 1 = 00000001
    # 2 = 00000010
    # 3 = 00000011
    # 4 = 00000100
    # 5 = 00000101
    # 6 = 00000110
    # 7 = 00000111
    # 8 = 00001000
    # 9 = 00001001
    # 10 = 00001010
    # 11 = 00001011
    # 12 = 00001100 
    # 13 = 00001101
    # logical operator(논리 연산자)의 종류
    # pyhton에서의 논리연산자의 사용법
    # python에서의 반복문 문법
    # python에서의 조건문 문법
    # python 연산자 사용법
def main():
    #이게 뭐한거임?
    #할당만 한거임
    #입력한거를 num 이란 변수에 할당한거임
    # a , b 이 워딩에 집중하지 말고
    # a , b 변수를 띄어쓰기 기준으로 입력받는당
    # 4 5 이렇게 입력하고 엔타를 치면
    # a = 4 , b = 5 로 할당이 됨 
    a , b = input().split()
    a = int(a)
    b = int(b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)  
    print(a % b)
if __name__ == "__main__":
    main()
