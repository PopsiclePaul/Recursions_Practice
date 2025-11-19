A = int(input('enter no 1: '))
B = int(input('enter no 2: '))

def gcd(A,B):
    if B%A == 0:
        return A
    else:
        return gcd(B,B%A)
    

print(gcd(A,B))
