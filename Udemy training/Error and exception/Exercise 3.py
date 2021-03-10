def ask():
    while True:
        try:
            entry = int(input("Please provide an number:"))
        except:
            print("An error occured! Please provide a number to proceed:")
        else:
            entry = entry **2
            print(f"Thank you, your number squarred is {entry}")
            break

    ask()