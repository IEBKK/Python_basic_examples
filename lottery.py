# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:02:45 2019

@author: ganze
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:37:18 2019

@author: ganze
"""

from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    
    lotto_numbs = []
    # 6개의 요소가 있을때까지 반복
    while len(lotto_numbs) < 6:
        # 새로 뽑은 수가 lotto_numbs에 없을 경우에만 추가
        new_number = randint(1, 45)
        if new_number not in lotto_numbs:
            lotto_numbs.append(new_number)
    lotto_numbs = sorted(lotto_numbs)     
    #print(lotto_numbs)    

    return lotto_numbs
    
    

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    
    winning_numbs = generate_numbers()
    while len(winning_numbs) < 7:
        bonus_numbs = randint(1, 45)
        if bonus_numbs not in winning_numbs:
            winning_numbs.append(bonus_numbs)
    
    # 리스트 리턴
    return winning_numbs
        
        

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
        
    # 두 리스트 사이에 겹치는 번호 갯수
    ##index = 0
    winning_count = 0
    # 두 리스트 길이 맞추기
    ##get_list = [int(len(list1)), int(len(list2))]
    ##max_list = max(get_list)
    ##while len(list1) != max_list:
        ##list1.append('')
    ##while len(list2) != max_list:
        ##list2.append('')
    # 공통 원소갯수 카운트    
    for element in list1:
        if element in list2[0:-1]:
            winning_count = winning_count + 1
        

    return winning_count

    

# 로또 등수 확인하기
    #numbers는 게임스타일 입력
def check(numbers, winning_numbers):
      
    #게임 스타일에 따른 참가자의 번호 6개    
    #numbers = generate_numbers()
    #winning_numbers = draw_winning_numbers()    
    count = count_matching_numbers(numbers, winning_numbers)
    money = 0
                       
    if winning_numbers[-1] in numbers and count == 5:
        print("2 등 축하드립니다!! 뽑은 번호 5개와 일반 번호 5개 일치, 그리고 번호 1개와 보너스 번호 일치 (5천만원)")
        money = 50000000
    
    elif count == 6:
        print("1 등 축하드립니다!! 뽑은 번호 6개와 일반 번호 6개 모두 일치 (10억원)")
        money = 1000000000
    
    elif count == 5:
        print("3 등 축하드립니다!! 뽑은 번호 5개와 일반 번호 5개 일치 (100만원)")
        money = 1000000
    elif count == 4:
        print("4 등 축하드립니다!! 뽑은 번호 4개와 일반 번호 4개 일치 (5만원)")
        money = 50000
    elif count == 3:
        print("5 등 축하드립니다!! 뽑은 번호 3개와 일반 번호 3개 일치 (5천원)")
        money = 5000   
    else:
        print("아쉽네요. 꽝입니다.")
        money = 0
        
    
    return money
        
        
 #등수 판별
"""
    if count == 6:
        i = 0
        for i in range(0, 6):
            if numbers[i] == winning_numbers[i]:
                print("1 등 축하드립니다!! 뽑은 번호 6개와 일반 번호 6개 모두 일치 (10억원)")
                money = 1000000000
            else:
                print("2 등 축하드립니다!! 뽑은 번호 5개와 일반 번호 5개 일치, 그리고 번호 1개와 보너스 번호 일치 (5천만원)")
                money = 50000000
    elif count == 5:
        print("3 등 축하드립니다!! 뽑은 번호 5개와 일반 번호 5개 일치 (100만원)")
        money = 1000000
    elif count == 4:
        print("4 등 축하드립니다!! 뽑은 번호 4개와 일반 번호 4개 일치 (5만원)")
        money = 50000
    elif count == 3:
        print("5 등 축하드립니다!! 뽑은 번호 3개와 일반 번호 3개 일치 (5천원)")
        money = 5000
    else:
        print("아쉽네요. 꽝입니다.")
        money = 0
        
    return money
"""      
    