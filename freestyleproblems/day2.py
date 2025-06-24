def fib_gen(x):
    if x < 1:
        return "Invalid"
    elif x == 1:
        return [0]
    elif x == 2:
        return [0,1]
    else:
        arry = []
        a = 0
        b = 1
        arry.append(a)
        arry.append(b)
        for i in range(0, x-2):
            arry.append(a + b)
            tempa = a
            tempb = b
            b = tempa+b
            a = tempb
        return arry

print(fib_gen(10))

my_array = [1,2,3,4,5,6,7]
my_aarray_2 = [1,2,3,4,5,6]
# Return index where value is found
def bin_search(arr, x):
    # these are indexes
    low = 0
    mid = len(arr) // 2
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        print(low,high,mid, arr)
        if(arr[mid] < x):
            low = mid + 1

        elif(arr[mid] > x):
            high = mid - 1
        
        else:
            return mid
        
        print(low,mid,high)
    return -1
        
print(bin_search(my_array, 5))
print(bin_search(my_array, 5))

        
