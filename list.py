# list is orderred collection of data 
# list is mutable(list can be changed/edited)

Marks=[600,620,720,700,400,300,720];
print(Marks);
Student=["Prannav","Meet","Nidhi","Jainam","JainamB","MeetP","Araham"];
print(Student);
print(Marks[2]);
print(Student[1:5]);

# list elements Searching
if "prannav" in Student:
    print("yes");
else:
    print("no");


# list Comprehension
Numbers=[i for i in range(10)];
print(Numbers)

Even=[i for i in range(100) if i%2==0];
print(Even);