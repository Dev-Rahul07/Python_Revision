# Exception Handling
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("Invalid input")
finally:
    print("Done")
