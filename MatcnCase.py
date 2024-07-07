#match case is just like switch case in C++,java etc
#match case does not contain break statments
y=89;
x=int(input("Enter number between 0 to 2"));
match x:
    case 0:
        print("number entered is zero");
    case 1:
        print("number entered is one");
    case _:
        print("number entered is two or grter than that");

#empty case with if-condition
    # case _ if y!=50:
        # print(y,"is not equal to 50");

