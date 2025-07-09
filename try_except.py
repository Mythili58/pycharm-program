def divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("You can't divide by zero1")
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
divide(a,b)