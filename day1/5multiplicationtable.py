#algorithm
"""
start 
prompt the user to enter a number
read the input and store it as a numeric value(integer or float)
for i from 1 to 10 (inclusive)
-compute product = number *1
-print the equation in the format : number *i = product
END"""


def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")
    

def main():
    n = float(input("Enter a number: "))
    print_multiplication_table(n)

if __name__ == "__main__":
    main()