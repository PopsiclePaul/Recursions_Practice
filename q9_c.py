n = int(input('enter no of lines: '))
a = 1

def pattern(a,n):
    if n == a:
        print(n*str(n),end = '')
        print()
    else:
        print(a*str(a),end = '')
        print()
        return pattern(a+1,n)
    
pattern(a,n)