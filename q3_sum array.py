import array as arr

arr1 = arr.array('i',[1,2,3,4,5,6,7,8,9])

def sum_arr(arr1):
    if len(arr1) == 0:
        return 0
    else:
        return arr1[0] + sum_arr(arr1[1:])

print(sum_arr(arr1))
