# -*- coding: euc-kr -*-


### 자료형


## 숫자 자료형

print(5)
print(-10)
print(3.14)
print(5+3)
print(5*4)
print(3*(3+1))


## 문자열 자료형

print('abc')
print("a"*9)
print("ㅋ"*5)


## boolean 자료형 - 참/거짓

print(5>10)
print(True)
print(not True)
print(not (5>10))


## 변수

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 어른일까요?", is_adult)   # 쉼표는 공백 한 칸 포함


## 주석

# 한 줄 주석
''' 이렇게
하면
여러문장
주석처리'''
# 여러문장 선택 후 [ctrl] + '/' 누르면 일괄 주석처리





### 연산자


## 연산자

print(1+1) 
print(2**3) # 2^3=8
print(4//3) # 몫 1

print(10 > 3) # True
print(4 == 2) # False

print(1 != 3) # True
print((3 > 0) & (3 < 5)) # True
print((3 > 0) | (3 < 5)) # True
print(5 > 4 > 7) # False


## 간단한 수식

print(2 + 3 * 4)

number = 2 + 3 * 4
print(number)

number += 2 # 16
print(number)

number %= 2 # 0
print(number)


## 숫자 처리 함수

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3 (반올림)

from math import *
print(floor(4.99)) # 4 (내림)
print(ceil(3.14)) # 4 (올림)
print(sqrt(16)) # 4.0 (제곱근)


## 랜덤 함수

from random import * 
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 정수값 생성

print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 정수값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 정수값 생성





### 문자열 처리


## 문자열

sentence = '나는 소년입니다'
print(sentence)

sentence2 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence2)


## 슬라이싱

jumin = "990120-1234567"

print("성별 : " + jumin[7]) 
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리(뒤부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지


## 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 모든 문자를 소문자로
print(python.upper()) # 모든 문자를 대문자로
print(python[0].isupper()) # []번째 문자가 대문자인지 
print(len(python)) # 문자열 길이 출력
print(python.replace("Python", "Java")) # 문자열 대체

index = python.index("n") # n이라는 글자가 몇번째인지
print(index) # 5
index = python.index("n", index + 1) # 시작위치(index + 1) 지정
print(index) # 15

print(python.find("Java")) # 문자열 찾기 -> 없으면 -1 출력
# print(python.index("Java")) # 문자열 찾기 -> 없으면 오류 발생

print(python.count("n")) # 해당 문자 개수


## 문자열 포맷

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간")) # 나는 빨간색과 파란색을 좋아해요.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4 (v 3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


## 탈출 문자

# \n : 줄바꿈
print("백문이 불여일견\n 백견이 불여일타")

# \" \' : 문장 내에서 따옴표
print("저는 \"나도코딩\"입니다.") # 저는 "나도코딩"입니다.
print("저는 \'나도코딩\'입니다.") # 저는 "나도코딩"입니다.

# \\ : 문장 내에서 \
print("C:\\Users\\user\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple") # Red   Apple





### 자료구조


## 리스트

# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호")) # 1

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']

# 정형돈씨를 유재석 / 조세호 사이에 태워 봄
subway.insert(1, "정형돈")
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())

# 같은 이름의 사람이 몇 명 있는지 확인
print(subway.count("유재석")) # 1

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) # []

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]

# 리스트 확장
num_list = [1, 2, 3, 4, 5]
num_list.extend(mix_list)
print(num_list) # [1, 2, 3, 4, 5, '조세호', 20, True]


## 사전

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 오류 (프로그램 종료)

print(cabinet.get(5)) # None
print(cabinet.get(5, "사용 가능")) # 사용 가능

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국" 
cabinet["C-20"] = "조세호" 
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())
 
# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)


## 튜플

# 변경되지 않는 목록을 사용 시 쓰임
# 리스트보다 속도가 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])

# menu.add("생선까스") # 오류 발생

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


## 세트

# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합
print(java | python) # {'유재석', '박명수', '김태호', '양세형'}
print(java.union(python)) # {'유재석', '박명수', '김태호', '양세형'}

# 차집합
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# 값 추가
python.add("김태호") 
print(python) # {'김태호', '유재석', '박명수'}

# 값 제거
java.remove("김태호")
print(java) # {'양세형', '유재석'}


## 자료구조의 변경

menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'주스', '우유', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # {'주스', '우유', '커피'} <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # {'주스', '우유', '커피'} <class 'tuple'>





### 제어문


## if

weather = "맑아요"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
    print("너무 더워요.")
# else:
#    print("너무 추워요.")


## for

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


## while

# while문 안의 조건이 만족할 때까지 계속 반복
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# 무한루프 - 강제종료는 [Ctrl] + C
# while True: 


## continue와 break

# continue : 밑의 문장 실행하지 않고, 다음 반복으로 진행
# break : 밑의 문장 실행하지 않고, 반복문 탈출


## 한 줄 for

# 1,2,3,4 앞에 100을 붙이기 -> 101,102,103,104
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students) # [8, 4, 10]

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']





### 함수


## 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


## 전달값과 반환값

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
print(balance)  
balance = withdraw(balance, 500)
print(balance)


## 기본값

def profile(name, age = 17, main_lang = "C"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")


## 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)


## 가변인자

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" "은 줄바꿈하지 않고 띄어쓰기만 한다는 의미
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "HTML")
profile("김태호", 25, "Python", "Java")


## 지역변수와 전역변수

# 지역변수 : 함수 내에서만 사용 가능
# 전역변수 : 프로그램 어디서든 사용 가능





### 입출력


## 표준입출력

print("Python", "Java", sep=",")
print("Python", "Java", sep=",", end="?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력 
print("Python", "Java", file=sys.stderr) # 표준 에러 처리

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") 

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) # 3칸 띄우고 빈 공간은 0으로 채움

# 사용자 입력을 통해서 값을 받으면 항상 문자열로 저장이 된다.
# answer = input("아무 값이나 입력하세요 : ") 
# print("입력하신 값은" + answer + "입니다.")


## 다양한 출력 포맷

# 빈자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 때는 +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

# 3자리마다 콤마를 찍고, 부호도 붙여주기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))


## 파일 입출력

# 파일 입력(쓰기)
#score_file = open("score.txt", "w", encoding="utf8")
#print("수학 : 0", file=score_file)
#print("영어 : 0", file=score_file)
#score_file.close()

# 존재하는 파일일 때 
#score_file = open("score.txt", "a", encoding="utf8")
#score_file.write("과학 : 80\n") # 줄바꿈 따로 명시해주어야 함
#score_file.close()

# 파일 출력(읽기)
#score_file = open("score.txt", "r", encoding="utf8")
#print(score_file.read())
#score_file.close()

# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
#score_file = open("score.txt", "r", encoding="utf8")
#print(score_file.readline()) 
#score_file.close()

# 파일의 길이를 모를 때
#score_file = open("score.txt", "r", encoding="utf8")
#while True:
#   line = score_file.readline()
#   if not line:
#        break
#   print(line)
#   score_file.close()

# 리스트에 넣어 처리
#score_file = open("score.txt", "r", encoding="utf8")
#lines = score_file.readlines() # list 형태로 저장
#for line in lines:
#   print(line, end="")
#   score_file.close()


## pickle

# 프로그램 상에서 사용하는 데이터를 파일 형태로 저장하는 것

#import pickle
#profile_file = open("profile.pickle", "wb", encoding="utf-8")
#profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
#print(profile)
#pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
#profile_file.close()

#profile_file = open("profile.pickle", "rb")
#profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
#print(profile)
#profile_file.close()


## with

#import pickle
#with open("profile.pickle", "rb") as profile_files:
#    print(pickle.load(profile_file))

#with open("study.txt", "w", encoding="utf8") as study_file:
#   study_file.write("파이썬 공부")

#with open("study.txt", "r", encoding="utf8") as study_file:
#   print(study_file.read())





### 클래스

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 30, 5)


## __init__

# 파이썬에서 생성되는 생성자
# 객체가 만들어질 때 자동으로 생성
# 객체 생성 시 __init__ 함수와 정의된 변수의 개수와 동일하게 정의를 해주어야 함
# marine3 = Unit("마린") # 오류 발생


## 멤버변수

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 외부에서 객체를 추가 생성하는 것도 가능
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True


## 메소드

# 기본 작성 과정은 함수와 같음
# 메소드의 첫 번째 매개변수는 반드시 self를 지정해야 함


## 상속

# 물려받는 것을 의미

# Unit 클래스에 있는 변수 모두 사용 가능
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.clocking = clocking


## 다중상속

# 여러 곳에서 상속을 받는 것을 의미
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

# 이와 같이 다중상속을 사용
# class FlyableAttackUnit(AttackUnit, Flyable): 


## 메소드 오버라이딩

# 파생클래스에서 기반클래스의 메소드를 새로 정의





### 예외처리