from time import sleep
import random
import os

def clear():
    return os.system("clear")

user = input("이름을 입력해 주세요: ") #유저네임 저장

print(f"{user}님 안녕하세요!")
print("게임 시작")
point = 0
while True:
    result = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    final_result = random.choice(result)
    sleep(1)
    print("point: ", point)
    print(final_result)
    ask = input(": ")
    if ask == final_result:
        point += 1
        print("correct")
        sleep(0.5)
        clear()
    elif ask == "log out":
        break
    else:
        point -= 1
        print("wrong")
        sleep(1)
        clear()

print("게임을 종료 합니다")