#1.write a program to print current date and time

#import time module
import time

##dd/mm/yy format
print("current date : "+time.strftime("%d-%m-%y"))
print("curent time :  "+time.strftime("%x"))

#2. Write a Python program which accepts the radius of a circle from the user and compute the area

radius=int(input("Enter the radius : "))
PI=3.14
area=PI*radius*radius
print("The area of the circle is : ",area)

#3.Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
first_nam=input("enter your first nane : ")
last_name=input("enter your last name :  ")
print("hii"," ",last_name," ",first_nam)

#4.Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

num=input("enter some commas separated numbers : ")
list=num.split(",")
tuple=tuple(list)
print("list of num : ",list)
print("tuple of num : ",tuple)

