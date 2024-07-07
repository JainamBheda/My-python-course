letter=("my name is {} and I am from {}");
name=("Jainam");
Country=("India");
print(letter.format(name,Country));

# Above code is for formating string which uses {} and .format() function 
# the above code is old method for formating

# f-string is new method of formating

print(f"My name is {name} and I am from {Country}");    #(variable):country (literal):India


