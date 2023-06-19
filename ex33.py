
def list_loop(num, increase):
    numbers = []

    for i in range(num):
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increase
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

list_loop(20, 2)
