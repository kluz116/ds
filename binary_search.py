import math
def binary_search(arr,targetItem):
    startIndex = 0
    endIndex = len(arr)-1

    while startIndex <= endIndex:

        midIndex = math.floor((startIndex+endIndex)/2)
     
        if arr[midIndex] == targetItem:
            return f'The Target item {targetItem} was found at position {midIndex} which is {arr[midIndex]}'
        
        elif  targetItem < arr[midIndex]: 
            endIndex = midIndex - 1 
        else:
            startIndex = midIndex + 1
            


y = [30,40,60,89,90,100,109,110,116]

print(binary_search(y,110))


    eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOlsibWNyYi1hcGkiXSwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sImV4cCI6MTcwNDAzMDA2MiwianRpIjoiZGNhZDMxNGQtN2I1OC00YmQ5LTlmZmUtNjZmNzRlYWE5ZGQ2IiwiY2xpZW50X2lkIjoiVFBsZWNQN1ZkYmxmNHl4cnJPelYxcVZvbWNPTUhzTGcifQ.octt98ztrbp4G6hTi3P6W20R08kw1C8mlp7I3ZIpUWs
