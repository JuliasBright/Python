# this sign is used to write comment in your code in order to keep track of you code
#python most common version are 2 and 3
#To start with python is very easy 
#the fist lesson [+,-,/,*]
#in order to write program here it litle bit different from python shell 
#in order to print any word or number the word(print is used)

#Addition:
print(2+2)
print(545446+545454)
print(25+(254+54))

#substraction:
print(5-5)
print(55-464)
print(9898-(5454-121))

#Dividing
print(5/5)
print(898/(5757+8742-447))

#Multiplication
print(8*8)
print(545/(55*555))

#Exponental (concentation)
# * it ussually written as multiplication only this quoted with mark to differentiate it
print(4* '5')
print(55* "5") #it doesnt matter what quote mark it is 


#this will print 5 by four time and not four times five,, remember when you see the quote mark that mearn we have change into \n string and not multiplication

#we can use this on any code requring numbers and that is including decimal points
#if you want to use text in python, we use strings
print("Example when we write sentence and it is too long we can use \n to break the sencence and make it two")
print("you cant use the break\n on numbers it will cause error especially when we do calculations")

#Input
input = ("Enter a name:")
print(input)

#you can use input to enter any code you want it to perform

input1 = ("Enter a name:")

input2 =  ("Enter another number:")

print("This is what you enter" + " " + 'input1' + " " + 'input2')

#to understand this more lest look to another example
#to get deep understand of this we have intergers,float and strings
#strings are word
#float are used to turn strings into numbers

print(int("4") + int("5")) 
#this will work because its only a number now lets say we want a user to have input we will say

print(float(input("Enter a number: ")) + float(input("Enter another number: ")))
#this can be used to enter any information to the code 
# another way to work around it isby
x = input("Enter a number: ")
print(x)
y = input("Enter another number: ")
print(y)

result = float(x) + float(y)
print(result)

#variables
# to assign varibale in python which plays a big role like any other programming language here are some examples
var = 5
print(var)
del var   #this delete the variable which you decleare before
var = 12
print(var)  #now it will print the new assigned variable 
#you can use this fow any code input you want