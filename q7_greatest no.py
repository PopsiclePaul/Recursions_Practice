lst1 = list(eval(input('enter list of nos: ')))
maxno = 0

def find_max(lst1,maxno):
    if len(lst1) == 0:
        return maxno
    else:
        if lst1[0]> maxno:
            maxno = lst1[0]
        return find_max(lst1[1:],maxno)
    
print(find_max(lst1,maxno))