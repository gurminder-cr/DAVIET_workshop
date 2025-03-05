# mutable- can change, heterogenous, indexed, ordered -[]

# li=[13,True,'hello',56,90,43]
# print(li)
# print(type(li))

# for i in li:
#     print(i)
    
l=[]
for i in range(0,20):
    if i%2==0:
        l.append(i)
    else:
        l.append(i**2)
print(l)

# list compre
# a=[i for i in range(0,20) if i%2==0]
a=[i if i%2==0 else i**2 for i in range(0,20) ]
print(a)
        
# b=[i for i in range(15) if i%3==0]
b=[i for i in a if i%3==0]
print(b)

a=[12,34,56,78]
b=[56,78,100,103]
# [56,78]

# [(56,56),(78,78)]

# tuple - (12,14,15)