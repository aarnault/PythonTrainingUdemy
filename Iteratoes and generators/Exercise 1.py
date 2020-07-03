def gensquares(N):
    for num in range(N):
        yield num**2

for x in gensquares(10):
    print(x)