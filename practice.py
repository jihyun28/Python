# -*- coding: euc-kr -*-


### �ڷ���


## ���� �ڷ���

print(5)
print(-10)
print(3.14)
print(5+3)
print(5*4)
print(3*(3+1))


## ���ڿ� �ڷ���

print('abc')
print("a"*9)
print("��"*5)


## boolean �ڷ��� - ��/����

print(5>10)
print(True)
print(not True)
print(not (5>10))


## ����

animal = "������"
name = "��ź��"
age = 4
hobby = "��å"
is_adult = age >= 3

print("�츮�� " + animal + "�� �̸��� " + name + "����")
print(name + "�� " + str(age) + "���̸�, " + hobby + "�� ���� �����ؿ�")
print(name, "�� ��ϱ��?", is_adult)   # ��ǥ�� ���� �� ĭ ����


## �ּ�

# �� �� �ּ�
''' �̷���
�ϸ�
��������
�ּ�ó��'''
# �������� ���� �� [ctrl] + '/' ������ �ϰ� �ּ�ó��





### ������


## ������

print(1+1) 
print(2**3) # 2^3=8
print(4//3) # �� 1

print(10 > 3) # True
print(4 == 2) # False

print(1 != 3) # True
print((3 > 0) & (3 < 5)) # True
print((3 > 0) | (3 < 5)) # True
print(5 > 4 > 7) # False


## ������ ����

print(2 + 3 * 4)

number = 2 + 3 * 4
print(number)

number += 2 # 16
print(number)

number %= 2 # 0
print(number)


## ���� ó�� �Լ�

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3 (�ݿø�)

from math import *
print(floor(4.99)) # 4 (����)
print(ceil(3.14)) # 4 (�ø�)
print(sqrt(16)) # 4.0 (������)


## ���� �Լ�

from random import * 
print(random()) # 0.0 ~ 1.0 �̸��� ������ �� ����
print(random() * 10) # 0.0 ~ 10.0 �̸��� ������ �� ����
print(int(random() * 10 + 1)) # 1 ~ 10 ������ ������ ������ ����

print(randrange(1, 45)) # 1 ~ 45 �̸��� ������ ������ ����
print(randint(1, 45)) # 1 ~ 45 ������ ������ ������ ����





### ���ڿ� ó��


## ���ڿ�

sentence = '���� �ҳ��Դϴ�'
print(sentence)

sentence2 = """
���� �ҳ��̰�, 
���̽��� ������
"""
print(sentence2)


## �����̽�

jumin = "990120-1234567"

print("���� : " + jumin[7]) 
print("�� : " + jumin[0:2]) # 0���� 2 �������� (0,1)
print("�� : " + jumin[2:4])
print("�� : " + jumin[4:6])

print("������� : " + jumin[:6]) # ó������ 6 ��������
print("�� 7�ڸ� : " + jumin[7:]) # 7���� ������
print("�� 7�ڸ�(�ں���) : " + jumin[-7:]) # �� �ڿ��� 7��°���� ������


## ���ڿ� ó�� �Լ�

python = "Python is Amazing"
print(python.lower()) # ��� ���ڸ� �ҹ��ڷ�
print(python.upper()) # ��� ���ڸ� �빮�ڷ�
print(python[0].isupper()) # []��° ���ڰ� �빮������ 
print(len(python)) # ���ڿ� ���� ���
print(python.replace("Python", "Java")) # ���ڿ� ��ü

index = python.index("n") # n�̶�� ���ڰ� ���°����
print(index) # 5
index = python.index("n", index + 1) # ������ġ(index + 1) ����
print(index) # 15

print(python.find("Java")) # ���ڿ� ã�� -> ������ -1 ���
# print(python.index("Java")) # ���ڿ� ã�� -> ������ ���� �߻�

print(python.count("n")) # �ش� ���� ����


## ���ڿ� ����

# ��� 1
print("���� %d���Դϴ�." % 20)
print("���� %s�� �����ؿ�." % "���̽�")
print("Apple�� %c�� �����ؿ�." % "A")
print("���� %s���� %s���� �����ؿ�." % ("�Ķ�", "����"))

# ��� 2
print("���� {}���Դϴ�.".format(20))
print("���� {}���� {}���� �����ؿ�." .format("�Ķ�", "����"))
print("���� {0}���� {1}���� �����ؿ�." .format("�Ķ�", "����")) # ���� �Ķ����� �������� �����ؿ�.
print("���� {1}���� {0}���� �����ؿ�." .format("�Ķ�", "����")) # ���� �������� �Ķ����� �����ؿ�.

# ��� 3
print("���� {age}���̸�, {color}���� �����ؿ�.".format(age = 20, color = "����"))
print("���� {age}���̸�, {color}���� �����ؿ�.".format(color = "����", age = 20))

# ��� 4 (v 3.6 �̻�)
age = 20
color = "����"
print(f"���� {age}���̸�, {color}���� �����ؿ�.")


## Ż�� ����

# \n : �ٹٲ�
print("�鹮�� �ҿ��ϰ�\n ����� �ҿ���Ÿ")

# \" \' : ���� ������ ����ǥ
print("���� \"�����ڵ�\"�Դϴ�.") # ���� "�����ڵ�"�Դϴ�.
print("���� \'�����ڵ�\'�Դϴ�.") # ���� "�����ڵ�"�Դϴ�.

# \\ : ���� ������ \
print("C:\\Users\\user\\Desktop\\PythonWorkspace>")

# \r : Ŀ���� �� ������ �̵�
print("Red Apple\rPine") # PineApple

# \b : �齺���̽� (�� ���� ����)
print("Redd\bApple") # RedApple

# \t : ��
print("Red\tApple") # Red   Apple





### �ڷᱸ��


## ����Ʈ

# ����ö ĭ���� 10��, 20��, 30��
subway = [10, 20, 30]
print(subway)

subway = ["���缮", "����ȣ", "�ڸ��"]
print(subway)

# ����ȣ���� �� ��° ĭ�� Ÿ�� �ִ°�?
print(subway.index("����ȣ")) # 1

# ���Ͼ��� ���� �����忡�� ���� ĭ�� Ž
subway.append("����")
print(subway) # ['���缮', '����ȣ', '�ڸ��', '����']

# ���������� ���缮 / ����ȣ ���̿� �¿� ��
subway.insert(1, "������")
print(subway) # ['���缮', '������', '����ȣ', '�ڸ��', '����']

# ����ö�� �ִ� ����� �� �� �ڿ��� ����
print(subway.pop())

# ���� �̸��� ����� �� �� �ִ��� Ȯ��
print(subway.count("���缮")) # 1

# ���ĵ� ����
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# ���� ������ ����
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# ��� �����
num_list.clear()
print(num_list) # []

# �پ��� �ڷ��� �Բ� ���
mix_list = ["����ȣ", 20, True]

# ����Ʈ Ȯ��
num_list = [1, 2, 3, 4, 5]
num_list.extend(mix_list)
print(num_list) # [1, 2, 3, 4, 5, '����ȣ', 20, True]


## ����

cabinet = {3:"���缮", 100:"����ȣ"}
print(cabinet[3]) # ���缮
print(cabinet[100]) # ����ȣ

print(cabinet.get(3)) # ���缮
# print(cabinet[5]) # ���� (���α׷� ����)

print(cabinet.get(5)) # None
print(cabinet.get(5, "��� ����")) # ��� ����

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"���缮", "B-100":"����ȣ"}
print(cabinet["A-3"])

# �� �մ�
print(cabinet) # {'A-3': '���缮', 'B-100': '����ȣ'}
cabinet["A-3"] = "������" 
cabinet["C-20"] = "����ȣ" 
print(cabinet) # {'A-3': '������', 'B-100': '����ȣ', 'C-20': '����ȣ'}

# �� �մ�
del cabinet["A-3"]
print(cabinet)

# key�鸸 ���
print(cabinet.keys())

# value�鸸 ���
print(cabinet.values())
 
# key, value ������ ���
print(cabinet.items())

# ����� ����
cabinet.clear()
print(cabinet)


## Ʃ��

# ������� �ʴ� ����� ��� �� ����
# ����Ʈ���� �ӵ��� ����

menu = ("���", "ġ��")
print(menu[0])

# menu.add("�����") # ���� �߻�

(name, age, hobby) = ("������", 20, "�ڵ�")
print(name, age, hobby)


## ��Ʈ

# ���� (set)
# �ߺ� �ȵ�, ���� ����

my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"���缮", "����ȣ", "�缼��"}
python = set(["���缮", "�ڸ��"])

# ������
print(java & python) # {'���缮'}
print(java.intersection(python)) # {'���缮'}

# ������
print(java | python) # {'���缮', '�ڸ��', '����ȣ', '�缼��'}
print(java.union(python)) # {'���缮', '�ڸ��', '����ȣ', '�缼��'}

# ������
print(java - python) # {'�缼��', '����ȣ'}
print(java.difference(python)) # {'�缼��', '����ȣ'}

# �� �߰�
python.add("����ȣ") 
print(python) # {'����ȣ', '���缮', '�ڸ��'}

# �� ����
java.remove("����ȣ")
print(java) # {'�缼��', '���缮'}


## �ڷᱸ���� ����

menu = {"Ŀ��", "����", "�ֽ�"}
print(menu, type(menu)) # {'�ֽ�', '����', 'Ŀ��'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # {'�ֽ�', '����', 'Ŀ��'} <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # {'�ֽ�', '����', 'Ŀ��'} <class 'tuple'>





### ���


## if

weather = "���ƿ�"
if weather == "��":
    print("����� ì�⼼��")
elif weather == "�̼�����":
    print("����ũ�� ì�⼼��")
else:
    print("�غ� �ʿ� �����")

# temp = int(input("����� ���?"))
# if 30 <= temp:
    print("�ʹ� ������.")
# else:
#    print("�ʹ� �߿���.")


## for

for waiting_no in [0, 1, 2, 3, 4]:
    print("����ȣ : {0}".format(waiting_no))

for waiting_no in range(5): # 0, 1, 2, 3, 4
    print("����ȣ : {0}".format(waiting_no))

for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("����ȣ : {0}".format(waiting_no))

starbucks = ["���̾��", "�丣", "���̿� �׷�Ʈ"]
for customer in starbucks:
    print("{0}, Ŀ�ǰ� �غ�Ǿ����ϴ�.".format(customer))


## while

# while�� ���� ������ ������ ������ ��� �ݺ�
customer = "�丣"
index = 5
while index >= 1:
    print("{0}, Ŀ�ǰ� �غ�Ǿ����ϴ�. {1}�� ���Ҿ��.".format(customer, index))
    index -= 1
    if index == 0:
        print("Ŀ�Ǵ� ���ó�еǾ����ϴ�.")

# ���ѷ��� - ��������� [Ctrl] + C
# while True: 


## continue�� break

# continue : ���� ���� �������� �ʰ�, ���� �ݺ����� ����
# break : ���� ���� �������� �ʰ�, �ݺ��� Ż��


## �� �� for

# 1,2,3,4 �տ� 100�� ���̱� -> 101,102,103,104
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

# �л� �̸��� ���̷� ��ȯ
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students) # [8, 4, 10]

# �л� �̸��� �빮�ڷ� ��ȯ
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']





### �Լ�


## �Լ�

def open_account():
    print("���ο� ���°� �����Ǿ����ϴ�.")

open_account()


## ���ް��� ��ȯ��

def deposit(balance, money): # �Ա�
    print("�Ա��� �Ϸ�Ǿ����ϴ�. �ܾ��� {0}���Դϴ�.".format(balance + money))
    return balance + money

def withdraw(balance, money): # ���
    if balance >= money:
        print("����� �Ϸ�Ǿ����ϴ�. �ܾ��� {0}���Դϴ�.".format(balance - money))
        return balance - money
    else:
        print("����� �Ϸ���� �ʾҽ��ϴ�. �ܾ��� {0}���Դϴ�.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
print(balance)  
balance = withdraw(balance, 500)
print(balance)


## �⺻��

def profile(name, age = 17, main_lang = "C"):
    print("�̸� : {0}\t���� : {1}\t�� ��� ��� : {2}".format(name, age, main_lang))

profile("���缮")
profile("����ȣ")


## Ű���尪

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="���缮", main_lang="���̽�", age=20)


## ��������

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("�̸� : {0}\t���� : {1}\t".format(name, age), end=" ") # end=" "�� �ٹٲ����� �ʰ� ���⸸ �Ѵٴ� �ǹ�
    print(lang1, lang2, lang3, lang4, lang5)

profile("���缮", 20, "Python", "Java", "C", "C++", "C#")

def profile(name, age, *language):
    print("�̸� : {0}\t���� : {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()

profile("���缮", 20, "Python", "Java", "C", "C++", "C#", "HTML")
profile("����ȣ", 25, "Python", "Java")


## ���������� ��������

# �������� : �Լ� �������� ��� ����
# �������� : ���α׷� ��𼭵� ��� ����





### �����


## ǥ�������

print("Python", "Java", sep=",")
print("Python", "Java", sep=",", end="?")

import sys
print("Python", "Java", file=sys.stdout) # ǥ�� ��� 
print("Python", "Java", file=sys.stderr) # ǥ�� ���� ó��

scores = {"����":0, "����":50, "�ڵ�":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") 

for num in range(1,21):
    print("����ȣ : " + str(num).zfill(3)) # 3ĭ ���� �� ������ 0���� ä��

# ����� �Է��� ���ؼ� ���� ������ �׻� ���ڿ��� ������ �ȴ�.
# answer = input("�ƹ� ���̳� �Է��ϼ��� : ") 
# print("�Է��Ͻ� ����" + answer + "�Դϴ�.")


## �پ��� ��� ����

# ���ڸ��� �� �������� �ΰ�, ������ ������ �ϵ�, �� 10�ڸ� ���� Ȯ��
print("{0: >10}".format(500))

# ����� ���� +�� ǥ��, ������ ���� -�� ǥ��
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# ���� �����ϰ�, ��ĭ�� _�� ä��
print("{0:_<10}".format(500))

# 3�ڸ����� �޸��� ����ֱ�
print("{0:,}".format(100000000000))

# 3�ڸ����� �޸��� ���, ��ȣ�� �ٿ��ֱ�
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3�ڸ����� �޸��� ����ֱ�, ��ȣ�� ���̰�, �ڸ��� Ȯ���ϱ�
# ���ڸ��� ^�� ä���ֱ�
print("{0:^<+30,}".format(100000000000))

# �Ҽ��� ���
print("{0:f}".format(5/3))

# �Ҽ��� Ư�� �ڸ��������� ǥ�� (�Ҽ��� 3° �ڸ����� �ݿø�)
print("{0:.2f}".format(5/3))


## ���� �����

# ���� �Է�(����)
#score_file = open("score.txt", "w", encoding="utf8")
#print("���� : 0", file=score_file)
#print("���� : 0", file=score_file)
#score_file.close()

# �����ϴ� ������ �� 
#score_file = open("score.txt", "a", encoding="utf8")
#score_file.write("���� : 80\n") # �ٹٲ� ���� ������־�� ��
#score_file.close()

# ���� ���(�б�)
#score_file = open("score.txt", "r", encoding="utf8")
#print(score_file.read())
#score_file.close()

# �ٺ��� �б�, �� �� �а� Ŀ���� ���� �ٷ� �̵�
#score_file = open("score.txt", "r", encoding="utf8")
#print(score_file.readline()) 
#score_file.close()

# ������ ���̸� �� ��
#score_file = open("score.txt", "r", encoding="utf8")
#while True:
#   line = score_file.readline()
#   if not line:
#        break
#   print(line)
#   score_file.close()

# ����Ʈ�� �־� ó��
#score_file = open("score.txt", "r", encoding="utf8")
#lines = score_file.readlines() # list ���·� ����
#for line in lines:
#   print(line, end="")
#   score_file.close()


## pickle

# ���α׷� �󿡼� ����ϴ� �����͸� ���� ���·� �����ϴ� ��

#import pickle
#profile_file = open("profile.pickle", "wb", encoding="utf-8")
#profile = {"�̸�":"�ڸ��", "����":30, "���":["�౸","����","�ڵ�"]}
#print(profile)
#pickle.dump(profile, profile_file) # profile�� �ִ� ������ file�� ����
#profile_file.close()

#profile_file = open("profile.pickle", "rb")
#profile = pickle.load(profile_file) # file�� �ִ� ������ profile�� �ҷ�����
#print(profile)
#profile_file.close()


## with

#import pickle
#with open("profile.pickle", "rb") as profile_files:
#    print(pickle.load(profile_file))

#with open("study.txt", "w", encoding="utf8") as study_file:
#   study_file.write("���̽� ����")

#with open("study.txt", "r", encoding="utf8") as study_file:
#   print(study_file.read())





### Ŭ����

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} ������ �����Ǿ����ϴ�.".format(self.name))
        print("ü�� {0}, ���ݷ� {1}".format(self.hp, self.damage))

marine1 = Unit("����", 40, 5)
marine2 = Unit("����", 40, 5)
tank = Unit("��ũ", 30, 5)


## __init__

# ���̽㿡�� �����Ǵ� ������
# ��ü�� ������� �� �ڵ����� ����
# ��ü ���� �� __init__ �Լ��� ���ǵ� ������ ������ �����ϰ� ���Ǹ� ���־�� ��
# marine3 = Unit("����") # ���� �߻�


## �������

wraith1 = Unit("���̽�", 80, 5)
print("���� �̸� : {0}, ���ݷ� : {1}".format(wraith1.name, wraith1.damage))

# �ܺο��� ��ü�� �߰� �����ϴ� �͵� ����
wraith2 = Unit("���̽�", 80, 5)
wraith2.clocking = True


## �޼ҵ�

# �⺻ �ۼ� ������ �Լ��� ����
# �޼ҵ��� ù ��° �Ű������� �ݵ�� self�� �����ؾ� ��


## ���

# �����޴� ���� �ǹ�

# Unit Ŭ������ �ִ� ���� ��� ��� ����
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.clocking = clocking


## ���߻��

# ���� ������ ����� �޴� ���� �ǹ�
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

# �̿� ���� ���߻���� ���
# class FlyableAttackUnit(AttackUnit, Flyable): 


## �޼ҵ� �������̵�

# �Ļ�Ŭ�������� ���Ŭ������ �޼ҵ带 ���� ����





### ����ó��