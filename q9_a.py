n = int(input('enter no of lines: '))

def pattern(n,a=1):
    if n == a:
        print(n*'*',end = '')
        print()
    else:
        print(a*'*',end = '')
        print()
        return pattern(n,a+1)
    

pattern(a,n)
