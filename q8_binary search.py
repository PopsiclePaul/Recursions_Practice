lst1 = list(eval(input('enter a list: ')))
no = int(input('no to search: '))
lst1.sort()
lower_index = 0
upper_index = len(lst1) - 1

def binary_search(lst1,no,lower_index,upper_index):
    if lower_index > upper_index:
        return -1 
    else:
        mid = (upper_index + lower_index)//2
        if no == lst1[mid]:
            return mid
        elif no > lst1[mid]:
            return binary_search(lst1,no,mid+1,upper_index)
        else:
            return binary_search(lst1,no,lower_index,mid-1)
    
print(binary_search(lst1,no,lower_index,upper_index))