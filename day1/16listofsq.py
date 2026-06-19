"""
ALGORITHM

Start

Initialize an empty list squares = [].

For i from 1 to 10 (inclusive):

Compute square = i * i

Append square to the list squares.

Print the list squares.

End"""



def create_squares(n):
    squares = []
    fir i in range(1, n + 1):
        squares.append(i * i)
    return squares


def main():
    result = create_squares(10)
    print(result)

if __name__ = "__main__"
    main()
