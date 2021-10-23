from functools import reduce

print("hello python")

data=[1,2,3,4,5]

data1=filter(lambda x : x% 2 ==0,data)
print(reduce(max,data1))