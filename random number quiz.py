from random import randint

chance = 4
num = randint(1, 20)

while chance >= 0:
    
    ans = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요:" % (chance)))
    
    if num == ans:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (4-chance))
        break
    elif num > ans:
        print("Up")
    elif num < ans:
        print("Down")
    chance = chance - 1
    
    if chance == 0 and num != ans:
        print("아쉽습니다. 정답은 %d였습니다." % (num))
        break
    
    
  