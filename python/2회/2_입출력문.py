#%% 출력문 - print() 란?
"""
print() 내장 함수
1. print() 함수는 괄호의 내용을 출력한다.
2. 출력하고자 하는 값이 여러개의 경우에는 콤마(,)로 구분한다.
3. 문자열을 출력하려면 홑따옴표('…') 또는 쌍따옴표("…")를 이용한다.
(홑따옴표 세 개('''… '''), 쌍따옴표 세 개("""... """) 사용 가능)

"""

# 간단한 예
# 1)
print("hello")

# 2)
names = 'Kim KunHee'
print(names)
print('Kim KunHee')

#%% check point 1
# 정해진 정답은 없습니다. ^^
# 1) 자신의 이름을 출력하세요.

# 2) 자신의 이메일을 출력하세요.

# 3) 간단한 자기소개(2줄) 출력하세요

#%% print() - 여러 변수를 출력

# math_score 라는 변수에 77 할당
math_score = 77
#science_score 라는 변수에 55 할당
science_score = 55
#english_score 라는 변수에 66 할당
english_score = 66

# 한 개의 변수 출력
# tab키 : 자동완성 기능
print(math_score)
print(science_score)
print(english_score)

# 여러 변수 출력
# 콤마로 구분해준다.
print(math_score science_score english score) # 에러발생
print(math_score, science_score, english_score)

#%% check point 2
# 1) name 변수에 이름 할당, email 변수에 자신의 이름, phone 변수에 전화번호를 할당하시오.

# 2) 위의 변수를 가지고 한 줄에 출력하시오


#%% print() - 문자열 + 변수값 출력
print("수학점수는 : ", math_score)

print("과학점수는 : ", science_score)

print("영어점수는 : ", english_score)

#%% check point 3
# 1) 수학점수, 과학점수, 영어점수를 print() 한 번만 사용하여 출력하세요.


#%% print() - 다양한 출력문 포맷
"""
한번에 문자열과 변수를 출력하려면 콤마(,)로 구분해야 한다.
매우 번거롭다...
손 쉽게 할 수 없을까?

print() 함수는 다양한 출력 포맷이 있다.
1) 콤마로 구분하여 출력
2) % 이용한 출력
3) .format 을 이용한 출력

다 몰라도 된다.!
3) .format을 이용한 출력을 사용하자!! (보기 편하다, 실무에서 사용)


"""

# .format 을 이용한 출력

print("수학점수는 : {}, 과학점수는 {}, 영어점수는 {} 이다 "
      .format(math_score, science_score, english_score))

print("수학점수는 : {0}, 과학점수는 {1}, 영어점수는 {2} 이다 "
      .format(math_score, science_score, english_score))

print("수학점수는 : {2}, 과학점수는 {2}, 영어점수는 {2} 이다 "
      .format(math_score, science_score, english_score))

# .format의 능력은 다음에 또 배워보도록 하자.

#%% check point 4
name = 'Sam-Kim'
age = 44

# print() 실행시 결과는?
# 1) print("My name is {0} and {1} years old.".format(name,age))

# 2) print("My name is {1} and {0} years old.".format(age,name))

# 3) print("My name is {0} and {2} years old.".format(name,age))


#%% print() - end='\n' 옵션
"""
함수는 여러 인수들을 가지고 있다. 보이진 않지만 print() 함수내의 end = '\n' 기능의
default 값은 '\n'으로 되어있다.

print() 함수 내에 사용하는 특수 문자 (이스케이프 문자라고도 함)
\\ : \ 문자 자체
\n : 개행문자(줄 바꿈)
\t : 탭 키
"""

# 1)
print('안녕하세요')
print('저는 홍길동입니다.')
# 2)
print('안녕하세요', end = '\n')
print('저는 홍길동입니다.', end = '\n')

print("안녕하세요", end=' ')
print("저는 홍길동입니다.")

#%% 입력문 - input()란 ?
"""
변수에 직접 입력하기 버겁다. 키보드로 입력할래!
"""

input()

name = input()

name

name = input("이름을 입력하세요 : ")

score = input("점수를 입력하세요 : ")

#%% 문제

# 1) 이름, 이메일, 전화보호를 입력받아 변수에 저장하시오.

# 2) 입력받은 변수를 아래의 출력결과와 동일하게 출력하시오.
"""
이름을 입력하세요 : 홍길동

이메일을 입력하세요 : abc@gmail.com

전화번호를 입력하세요 : 010-1234-4321

입력해주셔서 감사합니다.

이름 : 홍길동
이메일 : abc@gmail.com
전화번호 : 010-1234-4321
"""



#%% 정리
"""
print() 문
end='\n' 인수(옵션) 변경 가능

.format 으로 간단하게 출력


input() 
입력 받자!
