# DocString is just like comment which is used to describe function ,class or module 
# Note: (Docstring is not ignored****) like comments in python 
# it is string data type 

def Square(a):
    '''This function is for Square of desired numbers''';   
    print(a*a)
Square(5);    

print(Square.__doc__); #this is to see doc string in terminal

#doc string should be right below the function name