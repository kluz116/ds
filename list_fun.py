from functools import reduce
list_a = [2,3,4,5,6,7,8,10,45]
y = list(map(lambda x:x*2,list_a))
print(y)

yx = list(filter(lambda a:a%2==0,list_a))
print(yx)

my_pets = ['alfred', 'tabitha', 'william', 'arla']
print(list(map(str.upper,my_pets)))

final_value =reduce(lambda)