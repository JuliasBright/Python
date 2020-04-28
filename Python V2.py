#comparison
#Boolean value means used to compare two value, The primary value of boolean are (true and false)

my_boolean = 7

7 == 7 #this will produce the value of true

#other signs
7==7 #The two equal signs means 7 is equal to 7
7!=6 # this sign means is not equal to
7 <= 7 #means 7 is lower or equal to 7
7 >= 7 #means 7 is greate or equal to 7

#if/else
#if and else can be used within a statment to state the condition of the Code

if 10 == 12:
    print("Ten is equal to")
else:
    print("Ten is not equal to")

#list
#like we jnow about variables theres also list in python

my_list = [1,2,3,4]
print(my_list)

#we can declare many value as possble include strings in list

list = ["string", 1 [1,1,1,4],4.121]
print(list[1])

#count on list start from 0 to one
#to check items in list is and not is used 
list.append(45) #to add item
print(list)
print(len(list)) #to get number of items in the list

#insert is the other method of putting variable in the list
#but you must first declare the index of your insertion

index = 3
list.insert(11) 
print(list)

#or you can insert by 
list.insert(2,121) # note that the first no is the declaration of index on the list

#list range determines the number for defined to end defined
list.range(1,5)
print(list) #this will print number from 2 to 4 please note that range count start from 0 so it will look like
range[0] = 1
range[1] = 2 # and will continue until five

#also we can print range use the intergers value
print(list.range[1,5,2]) #this will print number by counting the last given number
print(list) #this will print list in range of 2,4 

#we can add things to the list this process is called loops

for word in list:
    print(list + "!")
#this will print all words plus !

