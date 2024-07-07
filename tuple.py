# tuple is unchangeble

tup=(1,2,3,4,5);
print(type(tup),tup);

tup2=(1)                     #this is integer because no comma after...
print(type(tup2),tup2);

tup3=(1,)                   #this is tuple because there is comma
print(type(tup3),tup3)

# Manipulating tuple
# We can change tuple to list for app[lying methods

temp=list(tup);
print(temp)
tup=tuple(temp);
print(tup);