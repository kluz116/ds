def buble_sort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    
    return arr

x =[3,2,5,1,4,8,7,10,9]
print(f'The Unsorted list is {x}')
print(f'The sorted list is {buble_sort(x)}')