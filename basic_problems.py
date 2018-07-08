#1.Write a Python program to display the first and last colors from the following list. Go to the editor
#color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
print("color_list = ",color_list[0]," ",color_list[-1])

#2.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

num=int(input("enter a number : "))
n1=int("%s"%(num))
n2=int("%s%s"%(num,num))
n3=int("%s%s%s"%(num,num,num))
print("n1+n2+n3 : ",n1,n2,n3)


#3.Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
year=int(input("enter year :  "))
month=int(input("enter month : "))
print(calendar.month(year,month))

#4. Write a Python program to get the volume of a sphere with radius 6

r=int(input("enter radius to calculate volume of sphere : "))
Pi=3.14
volume_sphere=(4/3)*Pi*r*r
print("volume of sphere : ",volume_sphere)

