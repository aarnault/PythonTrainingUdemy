try:
    for i in ['a','b','c']:
except TypeError:
    print("There is a type error!")
finally:
    print(i**2)