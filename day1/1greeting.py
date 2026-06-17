def greet_user(name: str, times: int) -> None:   #->None is used function does not give back a value
    """print a greeting to the user a specified number of times"""
    for __ in range(times):     #we are using _ because we don't need to use the loop variable it will take times in input
        print(f"Hello{name}!welcome")  #  F"......"(fstring ):allows you to insert the variables directly


if __name__ == "__main__":     
    user_name = input("enter your name:")
    user_times = int(input("enter the number of times to greet:"))
    greet_user(user_name, user_times)


"""algorithm of the program
define the great_user function in memory
check the if condition
pause and wait for you to type your name into the terminal save it as user_name
pause again and wait for the number user_times
call the greet_user function, passing it your name and number
inside the function start a loop that counts from 0 up to user_times - (because of range is times-1)
on each loop iteration print a greeting message
program finishes and exists"""