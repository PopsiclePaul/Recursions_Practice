N = int(input('enter a no: '))

def natural_sum(N):
    if N == 1:
        return 1
    else:
        return natural_sum(N-1)+N

print(natural_sum(N))
