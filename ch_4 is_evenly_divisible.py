# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:17:29 2019

@author: ganze
"""

##짝수인지 홀수인지 판단.
def is_evenly_divisible(number):
    even = number % 2  #짝수 또는 홀수 판별 기준
    return even == 0  #나머지 0이면 짝수 아니면 홀수

# 정답 출력
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))






# is_evenly_divisible 함수
def is_evenly_divisible(number):
    return number % 2 == 0

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))