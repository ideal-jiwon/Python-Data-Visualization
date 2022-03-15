print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
#참/거짓(boolean)
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not(5>10))
#변수 
#애완동물을 소개해주세요
animal = "강아지" #문자열은 "" 붙여야함
name = "연탄이"
age = 4 #숫자열은 "" 안붙여도됨
hobby = "산책"
is_adult = age >=3
#밑에변수를적용시킬때, 숫자는 앞에 str(  )을 붙여줘야함.
# + 대신에 , 로 사용해도 가능! => ","가 들어오면 띄어쓰기가됨.
''' 이렇게 하면 여러 문장이 주석처리됨''' 
#ctrl + / 해도됨

print("우리집 "+ animal +"의 이름은 "+ name +"이에요")
hobby = "공놀이"
print(name + "는" + str(age) + "살이며, " +hobby+ "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

#연산
print(1+1) 
print(3-2)
print(5*2)
print(6/3)
print(2**3)#2^3=8
print(5%3) #나머지값구하는거임 2
print(10%3) #1
print(5//3)#몫을 구하는 것 : 1
print(10//3)


print(10>3)#true
print(4 >=7 ) #false
print(10<3)
print(5<=5)

print(3==3)## 3과 3은 같다 (뒤와 앞은 같다)
print(4 == 2)
print(3+4==7)

print(1 != 3) #!= 는 앞뒤가 같지 않다
print(not(1 != 3))

print((3>0) and (3<5))
print(3>0) & (3<5))

print((3>0) or (3>5)) #뒤 중에 하나라도 true이면 나옴
print((3>0)|(3>5))
print(5>4>3)
print(5>4>7)


print(2+3*4)
print((2+3)*4)
number = 2+3*4
print(number)
number = number+2
print(number)
number += 2 #위에있는 문장과 같다
number *= 2
number /= 2
number -= 2
print(number)
number %= 2 #0
print(number)

print(abs(-5)) #절대값 : 5
print(pow(4, 2)) #4^2 =16
print(max(5,12)) #더 큰 최대값 = 12
print(min(5,12)) # 더 작은 값인 최소값
print(round(3,14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) #내림 =4
print(ceil(3.14)) #올림=4
print(sqrt(16)) #제곱근 = 4

#random 함수(무작위로 숫자를 뽑아냄)

from random import*

print(random()) #0.-0 ~ 1.0 미만의 임의의 값을 생성하는 것
print(random()*10) #0.0 ~ 10.0 미만의 임의의 값을 생성
print(int(random()*10)) #0 ~10 미만의 임의의 값을 생성
print(int(random()*10)) #0 ~10 미만의 임의의 값을 생성
print(int(random()*10)) #0 ~10 미만의 임의의 값을 생성
print(int(random()*10)+1)
print(int(random()*10)+1)
print(int(random()*10)+1)
print(int(random()*10)+1)

#로또값 만들기

print(int(random()*45) + 1) #1~45이하의 임의의 값을 생성
print(int(random()*45) + 1)
print(int(random()*45) + 1)
print(int(random()*45) + 1)
print(int(random()*45) + 1)
print(int(random()*45) + 1)

print(randrange(1,46)) #1부터 46 미만의 값을 생성하자!
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))

print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45)) #1~45이하의 임의의 값을 생성 


#문자열공부하기
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

##슬라이싱:필요한 정보만 잘라서 사용하기

jumin = "940723-2067418"

print("성별 : " + jumin[7])##[]몇번째 값을 가져올껀지!!0번째부터시작한다
print("연 : " + jumin[0:2]) #0부터 2직전까지! (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])##0안적어도됨
print("뒤 7자리 : " + jumin[7:14])##끝부분 안적으면 알아서 끝까지 계산을 해줌
print("뒤 7자리 (뒤에부터) :" +jumin[-7:])
#맨 뒤에서 7번째부터 끝까지 55:07

#문자열처리함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())#boolean
print(len(python))#길이 length
print(python.replace("Python","Java"))

index = python.index("n")##위치값을 구하는 방법
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("java"))##-1이 나오는데 변수가 포함되지 않았을때 나오는 것
#print(python.index("java"))##변수가 없으면 error
print("hi")

print(python.count("n"))##몇번나오는지계산하는거

##문자열포멧

print("a" + "b")
print("a", "b")

##""이외에 다른 문제 만드는 방법
#방법1 퍼센트로 만드는 법 
print("나는 %d살입니다." %20) #d는 정수값
print("나는 %s을 좋아해요."% "파이썬") #s=문자(얘는 문자 정수다 할수 있음!!)
print("Apple 은 %c 로 시작해요." %"A") #문자

print("나는 %s색과 %s색을 좋아해요" % ( "파란","빨간"))

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

#방법3
print("나는{age}살이며, {color}색을 좋아해요.".format(age=20, color="빨강"))

#방법4 (v3.6 이상부터만 가능)
age = 20
color = "빨간"
print(f"나는{age}살이며, {color}색을 좋아해요.") #f는 변수를 밑에 있는 곳에 적용하는것


#탈출문자 \n : 줄바뀜
print("백문이 불여일견 \n백견이 불여일타")
# \" \'
#저는 "나도코딩"입니다
print("저는 \"나도코딩\" 입니다.")

#\\ : 문장 내에서 => \
print("C:\\Users\\home\\Desktop\\pythonworkspace>")

# \r : 커서를 맨 앞으로 이동 원래 있던거를 replace하는거임
print("Red Apple\rPine")

#\b : 백스페이스 (한글자지우는거임)
print("Redd\bApple")

#\t : 탭
print("Red\tApple")


#리스트 : 객체의 집합

#지하철 칸별로 10명, 20명, 30명이 있다고 가정해보자!
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]

print(subway)

subway = ["포포", "레오", "지원"]

#레오가 몇번째 칸?
print(subway.index("레오")) #1번째칸

# 영균이가 다음 정류장에서 다음 칸에 탐.
subway.append("영균")
print(subway)

# 정형돈씨를 포포랑 레오 사이
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명 뒤에서 꺼냄.
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)


#같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("포포")
print(subway)
print(subway.count("포포"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list = [5,4,3,2,1]
mix_list = ["포포", 20, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)

#1:31:39 사전시작하는 곳 dictionary
#목욕탕에가서 열쇠를 받음 -> 그러면 사물함을 열수있는데-> 키에 해당하는 사물함을 열수있음-> 키에대한 중복 허용x

cabinet = {3:"유재석", 100: "김태호"} #key : 3 , value : 유재석
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
print(cabinet.get(5)) #그냥 하면 종료 get를 쓰면 none이라고 나옴
print(cabinet.get(5, "사용 가능"))
print("hi")


print(3 in cabinet) #true
print(5 in cabinet) #false

cabinet = {"A-3" : " 유재석" ,  "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["A-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력하는법
print(cabinet.keys())

#value들만 출력하는법
print(cabinet.values())

#key,value 쌍으로 출력하려면
print(cabinet.items())

#목욕탕이 폐점
cabinet.clear()
print(cabinet)

#변경되지않는 항목들을 사용할때 
#맛있는 돈까스집!

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") <- 추가 불가능!!

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국" , 20, "코딩")
print(name, age, hobby)


#집합(set)
#중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 출력하는 법 (java와 python 를 모두 할 수 있는 개발자)
print(java&python)
print(java.intersection(python))

#합집합(java도 할수 있거나 또는 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java는 할수 있는데 python 못하는 개발자)
print(java - python)
print(java.difference(python))

#교육을 받아서 python을 할 줄 아는 사람이 늘어날때
python.add("김태호")
print(python)

# java를 까먹음!!!
java.remove("김태호")
print(java)

#자료구조의 변경 tuple

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)#set에서 list으로 바꾸기
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


#상황마다 다른 코드 사용

weather = input("오늘 날씨는 어때요?")
# if 조건:
#     실행 명령문
#조건을 서로 서로 비교해서 결과가 도출되는 방식임.
if weather == "비" or weather=="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요,")

temp = int(input("기온은 어때요?"))
if 30 <= temp :
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추어요, 나가지 마세요")

