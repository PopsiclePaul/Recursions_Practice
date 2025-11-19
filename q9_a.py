n = int(input('enter no of lines: '))
a = 1

def pattern(a,n):
    if n == a:
        print(n*'*',end = '')
        print()
    else:
        print(a*'*',end = '')
        print()
        return pattern(a+1,n)
    
pattern(a,n)