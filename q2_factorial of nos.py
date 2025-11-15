N = int(input('enter a no: '))

def factorial_no(N):
    if N == 0:
        return 1
    else:
        return factorial_no(N-1)*N

print(factorial_no(N))
