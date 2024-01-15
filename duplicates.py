
def _removeDup(arr):
    unique_list = []
    for i in arr:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


x = [2,4,5,2,3,6,7,3,3]
print(f'List before {x}')
print(_removeDup(x))
print(set(x))
