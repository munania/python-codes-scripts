import math

def sqrt():
    print("Input number to square root")
    number=int(input("Number: "))
    print("The square root of your number is: " + str(float(math.sqrt(number))))


def square():
    print("Number to square")
    number2 = int(input("Number"))
    print("The square of your number is: " + str(int(number2*number2)))


def main():
    print("""
    What problem do you want to solve today ?
    
    [1] - Calculate square root of a number
    [2] - Calculate the square of a number
    [3] - Exit
    """)

    action = input("Choose an option to calculate: ")

    if action == '1':
        sqrt()
    elif action == '2':
        square()
    elif action == '3':
        exit()
    else:
        print("Choose viable option")

main()