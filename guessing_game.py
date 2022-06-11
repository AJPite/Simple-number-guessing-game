import random
n = random.randint(1, 100)
print('I know a secret number between 1 and 100. Can you guess what it is?')
while True:
    ans = int(input('Enter your guess (0 to exit): '))
    if ans == n:
        print('Success! You win!')
        print('I know a cooler number between 1 and 100. Can you guess what it is?')
        n = random.randint(1, 100)
    elif ans > n:
        print('Too high.')
    elif ans == 0:
        break
    else:
        print('Too low.')
