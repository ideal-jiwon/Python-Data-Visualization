 #가변인자를 이용한 함수이용

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#      print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")#프린트가 끝날때 줄바꿈안하고 ""으로 끝남
#      print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")#프린트가 끝날때 줄바꿈안하고 ""으로 끝남
     for lang in language :
         print(lang, end=" ")
         print()

profile("유재석", 20, "python", "Java", "C", "C++", "C#", "javascript")
profile("김태호", 25, "k" , "s")

# 위와 같은 상황에서 할 수 있는 언어가 늘어나거나 추가적으로 " " 를 추가해야하는 상황이 생기는데 이때 코드 만드는것을 좀더 편하게 하기 위해서 
#쓰는 것이 가변인자라고 함

#지역변수와 전역변수 ( 함수내에서만 쓸 수 있는것 /모든 공간에서 다 쓸 수 있는 것)

gun = 10 #2:53

def checkpoint (soldiers) : #경계근무
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers) : 
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun#위에 공식에 대입 후 다시 돌아와서 다시 밑으로 print에 이어짐

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계근 무나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))


##표준입출력

print("python","java", sep=" , ", end="?") #end : 한줄에 다 나오게됨! end는 끝부분을 ?으로 바꿔줘!
print("무엇이 더 재밌을까요?")

import sys
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr) #따로 에러처리 가능

#출력포멧

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items() : 
     #print(subject, score)
     print(subject.ljust(8), str(score).rjust(4), sep=":") #왼쪽에서 8번가는것 ljust(8)

#은행에 갔을때 대기순번표
#001.002.003.004.~~~ 이런 순임 

for num in range(1,21) : 
     print ("대기번호 : " + str(num).zfill(3)) #3개만큼의 공간을 차지하고 값이 없는 부분은 0으로
    
#표준입력

# answer = input("아무 값이나 입력하세요 : ")
# answer = 10
# print(type(answer)) 
# print("입력하신 값은" + answer + "입니다.")


#다양한 출력포멧
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐, + 로 표시, 음수일땐 - 로 표시
print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_>10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000))
# 3자리 마다 콤마를 찍어주기, +- 보호도 붙이기
print("{0:+,}".format(-10000000000))
#3자리마다 콤마를 찍어주기, 부호도 붙이고, 자리수도 확보
#돈이 많으면 행복하니까 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수까지만 표시하고 싶어!(소수점3째 자리에서 반올림!)
print("{0:.2f}".format(5/3))

#파일입출력
# score_file = open("score.txt","w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write(" \n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) #줄별로 읽기, 한줄로 읽고 커서는 다음 줄로 이동
print(score_file.readline()) #줄별로 읽기, 한줄로 읽고 커서는 다음 줄로 이동
print(score_file.readline()) #줄별로 읽기, 한줄로 읽고 커서는 다음 줄로 이동
print(score_file.readline()) #줄별로 읽기, 한줄로 읽고 커서는 다음 줄로 이동
score_file.close()

#다음사람이 가지고 온 파일 읽기-반복문
score_file = open("score.txt", "r", encoding="utf8")
while True : 
    line = score_file.readline()
    if not line : 
        break 
    print(line) #줄바꿈 x  end = ""
score_file.close()

#list에 넣어서 정리하기 3:26

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장하기
for line in lines :
    print(line, end="")

score_file.close()


#pickle 
#저장하고 변수에 저장해서 오픈
import pickle
profile_file = open("profile.pickle", "wb") #피클을 쓰려면 항상 바이너리 해주고 encodingx
profile = {"이름" : "박명수", "나이" : 30, "취미": ["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()


profile_file = open("profile.pickle", "rb") #읽기용
profile = pickle.load(profile_file) #파일에 있는 정보를 프로필에 불러오기
print(profile)
profile_file.close()


#read ((저장하고 변수 만들어서 불러오기))
import pickle
with open("profile.pickle","rb") as profile_file: #profile_file이라는 변수에 저장
    print(pickle.load(profile_file)) #저장한거 불러오기


with open("study.txt", "w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
    

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


#마린 : 공격 유닛, 군인, 총을 쏩니다
name = "마린"
hp = 40 #유닛의 채력 
damage = 5 #유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("채력 {0}", "공격력 {1}\n".format(hp,damage) )

#탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드/시즈모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("채력 {0}", "공격력 {1}\n".format(tank_hp,tank_damage) )

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("채력 {0}", "공격력 {1}\n".format(tank2_hp,tank2_damage) )

def attack(name, location, damage) : 
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage ))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank_damage)



