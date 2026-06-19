"""
###ALGORITHM###
define a function celsius to fahrenheit(c) that takes one parameter c (temperature in celsius).
===inside the function:
-compute fahrenheit = (c * 9/5) + 32
-return fahrenheit

===outside the function:
prompt the user to enter a temperature in celsius
read the input and convert it to a float
call celsius_to_fahrenheit() with the user's value and store the result
print the fahrenheit value

END
"""


def celsius_to_fahrenheit(c):
    return ( c * 9 / 5) + 32


def main(): 
    celsius = float(input("enter temperature in celsius :"))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f}degree celsius = {fehrenheit:.2f}degree fehrenheit")


if __name__=="__main__"
    main() -> None