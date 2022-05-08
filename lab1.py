import random

ans = random.randint(1, 10)
steps = 0

while True:
    x = int(input("take a guess between 1 to 10 : "))
    if ans == x:
        print("you win!!!")
        break
    else:
        if (x-ans)/ans * 100 > ans:
            print("you're a little above")
        else:
            print("you're a little below")
    steps += 1


print(f"you took {steps} steps")