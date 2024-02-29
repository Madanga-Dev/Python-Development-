##WEEK 1

print("Hello World")
##Variables

Name = "Emmanuel"
Age = 36
print (Name)
print(Age)

##Data Types in Python
Num=25
print(Num, "Is of type", type(Num))

##List Data type in Python []
students= ["Henrique", "Emmanuel ", "John"]
print(students)

## Access List Items using Index numbers
print(students[0])

##Tuple Data type in Python ()
Fruits=("Mango", "Orange", "Apple")
print(Fruits)
print(Fruits[1]) ## Access item

##Python String Data Type
Gender= "Male" 
print(Gender)

##Python Set Data Type
Grades = {45, 34, 89, "Students"}
print(Grades)
print(type(Grades)) 

##Python Dictionary Data Type - Keys and Values
Capital_city= {'Kenya':'Nairobi', 'Uganda':'Kampala'}
print(Capital_city)
print(Capital_city["Kenya"]) ## Access item using Keys and not values 

##Type conversion in Python  implicit and Explicit
##Implicit
num1 = 45
num2 = 5.67
num3= num1 + num2
print(type(num3))

##Explicit - uses int() , float(), str()

num4 = 45
print(type(num4))
num5=str(num3)
print(type(num5))

##Comments
##Single line and Multi-line Comments   - Use # at the beginning of every comment

#Basic Operations
#Arithmetic operators
#Assignment Operators
#Comparison Operators
#Logical Operators
#Bitwise Operators
#Special Operators

#1. Arithmetic operators
# used to perform mathematical operations like addition, subtraction, multiplication, etc
#2. Assignment Operators
X = 5
print(X)
X+=5
print(X)
X-=3
print(X)

#3. Python Comparison Operators. Used for decision making and loops
a= 5
b= 10
print(a>b)
print(a==b)
print(a!=b)
#4.Python Logical Operators . Used to check whether an expression is True or False. Used in decision making
print((a>b) and (b>a))
print((a>b) or (b>a))
print(not (b>a))

#5. Python Bitwise operators
print(a&b)
print(a|b)

#6. Python Special operators
#identity operator (is, is not) and the membership operator (in, not in)


##PRINTING OUTPUT AND COLLECTING USER INPUTS
#Printing Output
print('Good Morning!')
print("It is raining today right?")

print('Good Morning!', end =' ')
print("It is raining today right?")

print("It is raining?", sep=' ' "today right?")

#Print Python Variables and Literals
print(45)
number = 456
print(number)

#Print Concatenated Strings
print("This is "+ "Absolutely Amazing")


##Python Input   input() function
Marks = input("Enter your Marks: ")
print("Your Marks is", Marks)
##Exercise: Write a program that asks the user for their name, age, and location and then prints out a personalized message.