import string

def ispangram (strl, alphabet=string.ascii_lowercase):
# Create a set of the alphabet
alphaset=set(alphabet)
# Remove any spaces from the input string
strl=strl.replace(' ', '')
# Convert into all lowercase
strl=stlr.lower()
# Grab all unique letters from the string set()
strl=set(strl)
# Alphabet set == string set input
Return strl == alphaset