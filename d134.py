def factorial(n):
    if n <=1:
        return 1
    else:
        return n*factorial(n-1)

N,M = list(map(int,input().split()))

while (N!=0 or M!=0):
    C=factorial(N)//(factorial(N-M)*factorial(M))
    print(f'{N} things taken {M} at a time is {C} exactly.')
    N,M = list(map(int,input().split()))
