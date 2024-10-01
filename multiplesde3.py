num = 0

while num != 100:

    num += 1

    if num%3 == 0 and num%5 == 0:
        print("Girona")

    elif num%3 == 0:

        print("Coca")

    elif num%5 == 0:

        print("Cola")

    else:
        print(num)

        