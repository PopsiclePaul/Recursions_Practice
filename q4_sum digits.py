n = int(input('enter a no: '))

def sum_digits(n):
    if n%10 == 0:
        return 0
    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(n))
