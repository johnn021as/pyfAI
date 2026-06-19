""" algorithm
Start 
prompt the user to enter an integer
read the input and store it as an integer
check if the number is divisible by 2(i.e. , number % 2 == 0)
if true, print "even"
else, print "odd"
end"""


def even_or_odd(n):
    return "even" if n % 2 == 0 else "odd"

def main() :
    number = int(input("Enter an integer: "))
    print(even_or_odd(number))

if __name__ == "__main__" :
    main()
    