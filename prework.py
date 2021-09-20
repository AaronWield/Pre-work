# Python Prework 1-5
odd_nums = list(range(1,101))

for number in odd_nums:
    if number % 2 != 0:
        print(number)
    elif number % 2 == 0:
        print("Even")