num = 0

while num != 100:

    num += 1

    if num%3 == 0 and num%5 == 0:
        print("Madrid")

    elif num%3 == 0:

        print("Fizz")

    elif num%5 == 0:

        print("Cola")

    else:
        print(num)

        