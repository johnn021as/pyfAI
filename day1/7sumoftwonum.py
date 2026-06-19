"""
ALGORITHM
1. Start
2. Define a function add (a.b  ) that takes two parameters a and b
---inside the function :
compute sum = a+b
return the computed sum.
---outside the function :
prompt the to call add() with two values
print the returned sum
END"""


def add(a, b):
    return a + b

def main():
    num1 = float(input("Enter first number: "))
    total = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {total}")

if __name__ == "__main__":
    main()