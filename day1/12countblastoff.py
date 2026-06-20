"""
ALGORITHM
START
prompt the user to enter a positive integer
read the input and store it as an integer 'n'
check if n is positive (optional, but assumed valid input)
fir i from n down to 1 
--print the value of i
after the loop ends, print "BLAST OFF"
END
"""

def countdown(start):
    for i in range (start,0,-1):
        print(i)
    print("Blast off")



def main():
    number = int(input("enter a positive integer:"))
    countdown(number)


if __name__ == "__main__" :
    main()


