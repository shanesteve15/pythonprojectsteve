#operators
x=5
x+=3 #this is like saying x=x+3
x=x+3
x*=4 #x=x*4
print("my answer is",x)

#== sign maens equal to
y=20
y==34
print(y)


#!= not equal to
p=5
q=4
print(p!=q)

#conditional statements
age= 50
if age>=18:
    print("you are an adult")


# if...elif statements
if age>18:
    print("adult")
elif age<18:
    print("you are a child")


#if..elif..else statements

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")




#using the and statement
president_age=20
nationality="kenyan"
if president_age >=18 and nationality=="kenyan":
    print("you are a successful candidate")
else:
   print("you cannot be a candidaate")

#checking for an even and odd number
y=7
if y%2==0:
    print("even")
else:
    print("odd")

#casting
first_name="shane"
last_name="steve "
full_name=first_name+"  "+last_name
print(full_name)

#casting int int0 str
first_name="shane"
last_name=9
full_name=first_name+"  "+ str(last_name)
print(full_name)

#casting str into float
Bucket=20.0
book="50.0"
total=Bucket+float(book)
#casting float into str and adding the kenya shillings
result="total is"+" "+str(total)+" "+ "kenya shillings"
print(result)
#print(total)

#while loop--with break
i=1
while i<=6:
    #print(i)
    if i==4:
        break
    i+=1

#while loop--continue
i=0
while i<=6:
    i+=1
    if i==3:
        continue
    print(i)


#while loop input name
student_name=input("enter the student name")
while student_name=="":
    print("name not entered")
    student_name = input("enter the student name")
print("hello" , student_name)

##example nationality using while loop
visitors=int(input("enter the number of vistors"))
uganda=0
kenyan=0
counter=1
while counter<=visitors:
    nationality=input("enter nationality")
    if nationality=="kenyan":
        kenyan+=1
        print("allowed")
        counter+=1
    else:
        uganda+= 1
        print("not allowed")
        counter += 1
print("the number of visitors is",visitors)
print("the number of kenyan is",kenyan)
print("the number of uganda is",uganda)

#for loop in python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#the range fuction
for x in range(2,6,2):
  print(x)


#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  print(x)
  for y in fruits:
     print( "", y)

#list
color=["red"]
fruits=["apple", "banana", "cherry"]
for x in color:
    for y in fruits:
        for z in range(3):
          print(x,y)

student=list()
for i in range(3):
    student_name=input("enter name")
    student.append(student_name)
print(student)

#tuples
fruits=("apple","banana","orange","potatoes")
print(fruits)
myfruits=list(fruits)#convert the tuple to a list to change or add anything
myfruits[1]=("mangoes")#do ur changes ..we identify with index is (0-9)
myfruits.append("")
fruits=tuple(myfruits)#changing back to a tuple
print(fruits)

#sets
#check out the examples


#dictionaries
thisdict={"brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#functions in python
#creating a function
def addiction(x,y):
    return x+y
#calling the function
print(x+y)


def find_largest_number(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for nu in numbers[0:]:
        if nu > max_num:
            max_num = nu
    return max_num
my_list = [10, 5, 20, 15, 30,35]
largest_number = find_largest_number(my_list)
print("The largest number in the list is:",  largest_number )




student_name=("shane","kamau","liz","mercy","lewis")
y =list(student_name)
y.append("owen")
student_name =tuple(y)
print(student_name)

#repeated elememts in a list
my_list=("shane","kamau","liz","lewis","mercy","lewis")
repeated_elements =[]

for new in my_list:
    if my_list.count(new)>1:
        repeated_elements.append(new)
print(repeated_elements)

#removing a key and value to dont apper
machine={
    "model": "Ford",
     "speed": "100km/hr",
     "year":"2016"
}
machine.pop("speed")
print(machine)


#converting liist into dict
list1=["model","year","brand"]
list2=["mazda","2020","toyota"]
print(list1)
print(list2)
mydict=dict(zip(list1,list2))
print("mydict",mydict)


#repeated elememts in a list to appeaer once
my_list=("shane","kamau","liz","lewis","mercy","lewis")
repeated_elements =[]

for new in my_list:
    if my_list.count(new)>1:
        if new not in repeated_elements:
          repeated_elements.append(new)
print(repeated_elements)












