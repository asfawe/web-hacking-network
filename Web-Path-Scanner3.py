import copy

print("<<Shallow Copy>>")
a=[1,2,3,4]
b=a
print(b)
b[2]=10
print(b)
print(a)

print("<<Deep Copy>>")
c=[1,2,3,4]
d=copy.deepcopy(c)
print(c)
d[2]=10 
print(d)
print(c)


