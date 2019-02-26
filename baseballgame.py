# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 01:37:36 2019

@author: ganze
"""
"""
# 숫자야구 게임
from random import randint

# 0~9중 랜덤 숫자 3개 뽑기
numbers = []
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
while len(numbers) < 3:
    new_number = randint(0, 9)
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)
print(numbers)

# 숫자 3개 임의로 입력
count = 0   
while True:
    print("세 수를 하나씩 차례대로 입력하세요.")
    picks = []
    while len(picks) < 3:
        pick_number = int(input("%d번째 수를 입력하세요:" % (len(picks) + 1))) 
        if pick_number < 0 or pick_number > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        else:
            while pick_number in picks:
                print("중복되는 수 입니다. 다시 입력해주세요.")
                pick_number = int(input("%d번째 수를 입력하세요:" % (len(picks) + 1)))
                if pick_number < 0 or pick_number > 9:
                    print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
                    pick_number = int(input("%d번째 수를 입력하세요:" % (len(picks) + 1)))
        picks.append(pick_number)
    # 랜덤 숫자와 입력한 숫자 비교 (스트라이크, 볼 판별)
    strike = 0
    ball = 0
    i = 0
    while i < len(numbers): 
        if numbers[i] == picks[i]:
            strike += 1
        elif picks[i] in numbers:
            ball += 1
        i += 1
    print("%dS %dB \n" % (strike, ball))
    count += 1
    
    # 3 스트라이크면 게임 종료
    if strike == 3:
        print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (count))
        break
"""


# 숫자야구 게임
from random import randint

# 0~9중 랜덤 숫자 3개 뽑기
numbers = []
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
while len(numbers) < 3:
    new_number = randint(0, 9)
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)
print(numbers)

# 숫자 3개 임의로 입력
count = 0
strike = 0
   
while strike != 3:
    print("세 수를 하나씩 차례대로 입력하세요.")
    picks = []
    pick_number = 0
    while len(picks) < 3:
        pick_number = int(input("%d번째 수를 입력하세요:" % (len(picks) + 1))) 
        if pick_number < 0 or pick_number > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            
        elif pick_number in picks:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            
        elif pick_number not in picks:
            picks.append(pick_number)
            
    # 랜덤 숫자와 입력한 숫자 비교 (스트라이크, 볼 판별)
    
    ball = 0
    i = 0
    strike = 0
    while i < len(numbers): 
        if numbers[i] == picks[i]:
            strike += 1
        elif picks[i] in numbers:
            ball += 1
        i += 1
    print("%dS %dB \n" % (strike, ball))
    count += 1
    

print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (count))
    
###########################################
##모범 답안
from random import randint

# 번호 뽑기
def generate_numbers():
    # 숫자 3개를 보관할 리스트 생성
    numbers = []

    # 3개의 요소가 있을때까지 반복
    while len(numbers) < 3:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    # 리스트 리턴
    return numbers

# 정답 뽑기
ANSWER = generate_numbers()

# 변수 초기값 설정
tries = 0        # 시도 횟수
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수

# 번호를 모두 맞출때까지 반복
while strike_count < 3:
    # 번호 3개 입력 받기
    guess = []
    while len(guess) < 3:
        # 새로 입력한 수가 guess에 없을 경우에만 추가
        new_number = int(input("%d번째 수를 입력하세요: " % (len(guess) + 1)))

        # 범위를 벗어나면 설명 메시지 출력
        if new_number < 0 or new_number > 9:
            print("0에서 9까지의 수를 입력해주세요!")
        # 중복된 수를 입력하면 설명 메시지 출력
        elif new_number in guess:
            print("새로운 수를 입력해주세요!")
        # 타당한 값이면 guess에 추가
        else:
            guess.append(new_number)

    # 스트라이크, 볼 개수 세기
    strike_count = 0 # 스트라이크 개수
    ball_count = 0   # 볼 개수
    i = 0            # 인덱싱 변수

    while i < 3:
        if guess[i] == ANSWER[i]:
            strike_count = strike_count + 1
        elif guess[i] in ANSWER:
            ball_count = ball_count + 1
        i = i + 1

    print("%dS %dB" % (strike_count, ball_count))

    # 시도 횟수 추가
    tries = tries + 1

# 축하 메시지
print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries))
