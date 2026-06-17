"""Python file is saved in .py extension,
 it can be run on terminal by the command
   "python filename.py" 
   it can be used as interactive mode (good for experimenting.)
   """
#program1 understanding the Datatypes
name = "Alice"             #string(text)
age = 25                   #int
height = 5.6               #float
is_student = True         #boolean

#program2 Getting the user's input
user_name = input("enter your name")
# input ()always returns as a string

user_age = int(input("enter your age:"))
#convert string to integer with int()


#program 3 Printing the outputs

print("Hello")
print("Your name is ",user_name)
print(f"hello {user_name},you are {user_age} years old")
#f-string put varables inside{curly brackets}




#conditions (if/elif/else)
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("senior")



#program 6 Loops
#for loop
for i in range(7)
print(i)

#while loop
count = 0
while count<3
print("Still Counting")
count = count + 1





#Functions
def greet(name):
    """this is a docstring - explains the function"""
return f"hello{name}"


#Call the function
message = greet("john")
print(message)





#TYPE HINTS

def add(a: int,b: int) -> int:
    return a+b





#The if__name__=="__main__" Guard
def my_function():
    print("doing work")

if __name__== "__main__":
    #this only runs when you run this file directly,
    my_function()
    #it won't run if you import this file as a module in another file







#ERRORS AND TRY/EXCEPT (BASIC)
try:
    num = int(input("Enter number:  "))
    print(10 / num)
except ValueError:
    print("that's not a valid number")
except ZeroDivisionError:
    print("can't divide by zero")