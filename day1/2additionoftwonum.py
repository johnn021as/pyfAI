"""algorithm for the program 
the user to enter the first num
read the input and store it as a numeric value(integer or float)
the user to enter the second num
read the input and store it as a numeric value
compute the sum: sum = num1 + num2
display the result (the sum)
end"""

def get_number(prompt):
    return float(input(prompt))   #supports decimal


def main():
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    print(f"The sum of {a} and {b} is: {a + b}")

if __name__ == "__main__":
    main()