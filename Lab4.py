#2 Using the loop statement to print numbers from 0-10
for i in range(11):
    print(i, end=(""))
#3 Using the loop statement to print numbers from 1-10
for a in range(1,10):
    print(a,end=(""))
#4 Using loop statement to print numbers from 1-10 with an increment of 2
for b in range(1,10,2):
    print("b=",b)
#5 5,6 and 7 using the input function to ask user to enter the radius of a circle
import math
Radius=int(input("Enter the radius of a circle:"))
math.pi
Area=math.pi*Radius**2
print("Area=",Area)
#Step8,9 and 10 using the input funtion to calculate the are of a rectangle
length=int(input("Enter the length of a rectangle"))
width=int(input("Enter the width of a rectangle"))
Area_R=length*width
#11 Using the if and else statement to calculate the area of a rectangle
if Area_R>0:
    print("Area_R=",Area_R)
else:
    print("can't compute the area of a rectangle")