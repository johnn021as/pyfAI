def greet_user(name: str, times: int) -> None:
    """print a greeting to the user a specified number of times"""
    for __ in range(times - 1):
        print(f"Hello{name}!welcome")

if __name__ == "__main__":
    user_name = input("enter your name:")
    user_times = int(input("enter the number of times to greet:"))
    greet_user(user_name, user_times)