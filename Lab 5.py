
"""" Use the input function ask user enter number and cast the input to int"""
number1=int(input("Enter number1:"))
#3 Use the input variable to print number Tic if divisible by 3 and 5
for number1 in range(1,number1):
    if (number1 %3==0) and (number1 %5==0):
        print(number1, "Tic Tac")
# 4 Use the input variable to print number Tac if divisible by 3
    if(number1%3==0):
        print(number1,"Tic")
# 5 Use the if statement to check if input is divisible by 5
    if(number1%5==0):
        print(number1,"Tac")
# 6 Use the while loop statement to print numbers from 1-20
i=1
while i<21:
    i+=1
    print(i)
# 7 Use while loop statement to modify code from step 6
input1=int(input("Enter input1:"))
input1=1
while input1<16:
    input1+=1
    if input1%3==0 and input1%5==0:
        print(input1,"Tic Tac")
    elif input1%3==0:
        print(input1,"Tic")
    elif input1%5==0:
        print(input1,"Tac")
# 8 Use random_generator function to generate random numbers
import random
print(random.randint( 10, 40))
# 9 Creating value to store input
limit=5
while limit>0:
    user_value = int(input("Enter the value:"))
    if user_value>0:
        print(user_value,"\n Successful")
        break
    else:
        limit-=1
        print("invalid entry, please a valid value")

# 10
import random
user_value = int(input("Enter value: \n"))
main = random.randint(  1,user_value)
limit = 0
while True:
    limit+= 1
    my_number = int(input("first value: \n"))
    if my_number== main:
        print("perfect")
        break
    elif my_number != main:
        print("both numbers do not match")
        limit+= 1
    if limit == 5:
        print("exit!")

