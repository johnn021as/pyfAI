"""
ALGORITHM
START
prompt the user to enter a positive integer N
read the input and store it as an integer
initialise total = 0 (to accumulate the sum)
for i from 1 to N 
--add i to total
After the loop end , print the value of total
END
"""

def sum_1_to_n(N):
    total = 0
    for i in range(1, N + 1):
        total += i
    return total
    

def main():
    N = int(input("enter a positive integer:"))
    result = sum_1_to_n(N)
    print(f"the sum from 1 to {N} is {result}")


if __name__ == "__main__" :
    main()