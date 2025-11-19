n = int(input('enter no of lines: '))
a = 1

def pattern(a,n):
    if n == a:
        for i in range(1,n+1):
            print(i,end='')
        print()
    else:
        for i in range(1,a+1):
            print(i,end='')
        print()
        return pattern(a+1,n)
    
pattern(a,n)