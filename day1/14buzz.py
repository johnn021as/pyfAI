"""Algorithm
START
for i from 1 to 50 (inclusive)
-if i is divisible be both 3 and 5 , print"fizzbuzz"
else if i is divisible by 3,print"fizz"
else if i is divisible by 5,print"buzz"
else , print i
END
"""


def fizzbuzz(n):
    for i in range(1,n + 1):
        if i % 15 == 0:
            print("FiZZBuzz")
        elif i % 3 == 0:
            print("FiZZ")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



def main():
    fizzbuzz(50)



if __name__ = "__main__"
    main()