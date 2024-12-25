 # Tuple is an immutable data type.Here we discuss Tuple functions.

a=(1,45,342,3434,False,45,"Rohan")
print(len(a))  # no of elements in 'a'

print(a.count(45)) # how many 45 i.e. a element is there

print(a.index(342)) # index no of 342

print(1 in a) # check whether 1 is a element of tuple 'a' or not
print(2 in a) # check whether 2 is a element of tuple 'a' or not

b=(6,"Pritam",True)
c=a+b     # concatetion
print(c)

repeat = a*2
print(repeat)  # repeatation of a 2 times

s = a[2:5]
print(s)  # slicing

q,w,e,r,t,y,u = a
print(q,w,e,r,t,y,u) # unpacking