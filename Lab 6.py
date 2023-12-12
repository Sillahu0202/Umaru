
#Step 2 Develop a program to determine if its even or odd and also indicate if its prime or non prime
def is_prime(my_num):
    if my_num < 1:
        return False
    for i in range(2, my_num):
        if my_num % i == 0:
            return False
    return True

def main():
    while True:
        user_input = int(input("Enter number: "))

        if user_input > 0:
# Step 2 Check if the number is even or odd
            even_or_odd = "even" if user_input % 2 == 0 else "odd"

# Step 2 Check if the number is prime or nonprime
            prime_or_nonprime = "prime" if is_prime(user_input) else "nonprime"

            print(f"{user_input} is an {even_or_odd} number and it is {prime_or_nonprime}.")
            break
        else:
            print("Wrong input, enter a number >0.")

if __name__ == "__main__":
    main()
