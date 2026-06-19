"""Algoritm
start 
define a function max_of_two(a, b) that takes two parameters a and b
inside the function :
-if a > b , return a
-else (if a<=b), return b
outside the function :
call it with two numbers and print the result
END
"""


def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b        #implicit else 9if a <= b)
    

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    maximum = max_of_two(num1, num2)
    print(f"The maximum of {num1} and {num2} is: {maximum}")

if __name__ == "__main__":
    main()