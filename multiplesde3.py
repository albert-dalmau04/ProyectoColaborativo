num = 0

while num != 100:

    num += 1

    if num%3 == 0 and num%5 == 0:
        print("Barcelona")

    elif num%3 == 0:

        print("Coca")

    elif num%5 == 0:

        print("Buzz")

    else:
        print(num)

        