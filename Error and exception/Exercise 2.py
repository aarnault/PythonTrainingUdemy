try:
    x = 5
    y = 0

    z = x / y
except ZeroDivisionError:
    print("There is an error")
finally:
    print("All Done!")
