#Python variables
#Variables are containers for storing data values
#Creating Variables
#python has no command for declaring a variable
#example

x = 5
y = "NURI"
print(x)
print(y)

#Variables do not need to be daclared with any particular type,and can even change type after they have been set
#Example


x = 4 # x is of type int
x = "Memo" # x is now of type str
print(x)

#Casting ; If you want to specify the data type of variables, this can be done with casting
x= str(3) # x will be "3"
y= int(3) # y will be 3
z= float(3) # z will be 3.0

#How to get type of function
#put type() command
#Example
x= 3.1
y= "Yeah"
print(type(x))
print(type(y))
# x = "float"
# y = "str"