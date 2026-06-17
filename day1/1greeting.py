def greet_user(name: str, times: int) -> None:
    """Print a greeting repeated 'times' number of times."""
    for _ in range(times):
        print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_times = int(input("Enter a number: "))
    greet_user(user_name, user_times)