"""
ALGORITHM
    start
    define a function greet(name) that takes one parameter name
    inside the function
    return the string "Hello, " + name(or string)
    outside the function:
    CALL greet("Yourname") and print the result.
    END
    """
def greet(name):
    return f"Hello, {name}"

def main():
    user_name = input("Enter your name: "  )
    print(greet(user_name))

if __name__ == "__main__":
    main()