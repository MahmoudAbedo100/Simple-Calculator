def print_instructions():
    print("welcome to the calculator")
    print("provide 2 numbers and an operation type")


def add_2_numbers(number_1, number_2):
    return number_1 + number_2


def subtract_2_numbers(number_1, number_2):
    return number_1 - number_2


def multiply_2_numbers(number_1, number_2):
    return number_1 * number_2


def divide_2_numbers(number_1, number_2):
    return number_1 / number_2


print_instructions()
number_1 = float(input("what is your first number? "))
number_2 = float(input("what is your second number? "))
operation = int(input("operation type? (1 for addition," + \
                      " 2 for subtraction, 3 for multiplication," + \
                      " 4 for division)"))
if operation == 1:
    result = add_2_numbers(number_1, number_2)
elif operation == 2:
    result = subtract_2_numbers(number_1, number_2)
elif operation == 3:
    result = multiply_2_numbers(number_1, number_2)
elif operation == 4:
    if number_2 != 0:
        result = divide_2_numbers(number_1, number_2)
    else:
        print("division by zero is not possible!")
        exit()

else:
    print("operation number not valid")

print("Result: " + str(result))

print("made by mahmoud")