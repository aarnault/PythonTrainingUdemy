def up_low(s):
    lowercase = 0
    uppercase = 0
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f"Original String: {s}")
    print(f"Number of Lower Case: {lowercase}")
    print(f"Number of Upper Case: {uppercase}")
s = "Hello Mr. Rogers, how are you this fine Tuesday?"
up_low(s)

def up_low(s):
    d={"upper":0, "lower":0}
    for char in s:
        if char.isupper():
            d["upper"] += 1
        elif char.islower():
            d["lower"] += 1
        else:
            pass
    print(f"Original String: {s}")
    print(f"Number of Lower Case: {d['lower']}")
    print(f"Number of Upper Case: {d['upper']}")
s = "Hello Mr. Rogers, how are you this fine Tuesday?"
up_low(s)
