base = int(input('enter base: '))
exp = int(input('enter exponent: '))

def power(base,exp):
    if exp == 0:
        return 1
    else:
        return base*power(base,exp-1)

print(power(base,exp))