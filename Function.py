# to define function we use syntak :


# def function_name (parameter):
    # logic


def Calculate_mean(a,b):
    mean=(a+b)/2;
    print("the mean of ",a,"and",b,"is",mean);

def large(a,b):
    if(a>b):
        print(a,"is greater than",b)
    else:
        print("a is less than or equal to b");    




a=int(input());
b=int(input());
Calculate_mean(a,b);
large(a,b);