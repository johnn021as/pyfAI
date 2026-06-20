"""

Start

Import the random module.

Generate a secret number: secret = random.randint(1, 10).

Initialize guess = None (or any value not equal to secret).

While guess != secret:

Prompt the user to enter their guess.

Read the input and convert it to an integer.

If guess < secret, print "Too low".

Else if guess > secret, print "Too high".

When the loop exits (correct guess), print "Correct!" (or a similar message).

End

"""

import random 


def guess_the_num():
    secret = random.randint(1,100)
    print("i'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("your guess :"))
        if guess < secret:
            print("too low")
        elif guess>secret:
            print("toohigh")
        else:
            print("correct! you got it!")
            break




if __name__ == "__main__":
    guess_the_num()