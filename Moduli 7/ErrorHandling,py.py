# try:
#     result=10/0
#
# except ZeroDivisionError:
#     print("Opss! Tried to divide by zero!")
#
#
# fruits = {
#     "apple": 5,
#     "Orange": 3,
#     "banana": 7
# }
#
# try:
#     print(fruits["cherry"])
#
# except KeyError:
#     print("The key does not match in the dictionary")
#
#
# text = "This is not a number"
#
# try:
#     text_to_int = int(text)
#
# except Exception as e:
#     print("An error occurred", e)
#
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("Division by 0")
# else:
#     print("Division successful. Result=", result)
#
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("We have an error, we cant divide by 0")
# finally:
#     print("Finally blok executed")
#
# def divide_numbers(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("You to tried to divide by 0")
#     except TypeError:
#         print("Invalid type for division")
#     except Exception as e:
#         print("Unexpected error", e)
#     else:
#         print("The result is: ", result)
#
# divide_numbers(10,2)
# divide_numbers(10, 0)
# divide_numbers(10, '2')

def challenge(number1, number2, operator):

    if operator=="+":
        return number1+number2
    elif operator=="-":
        return number1 - number2
    elif operator=="*":
        return number1 * number2
    elif operator=="/":
        return number1 / number2
    else:
        raise ValueError("Invalid operator")

try:
    number1 = float(input("Shtyp numrin 1: "))
    number2 = float(input("Shtyp numrin 2: "))
    operator = input("Enter an operator (+,-,*,/): ")
    result = challenge(number1, number2, operator)
    print("The result of the operations is", result)

except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("You tried to divide by 0")
except Exception as e:
    print("There an error", e)
finally:
    print("The code was executed")