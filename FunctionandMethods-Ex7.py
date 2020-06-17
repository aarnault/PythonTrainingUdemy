import string

def ispangram (strl, alphabet=string.ascii_lowercase):
    for letter in strl:
        if letter not in alphabet:
            return False
        else:
            return True