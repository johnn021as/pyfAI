"""
ALGORITHM
Start
initialize an empty list numbers = [].
fir i from 1 to 5 (inclusive)
--prompt the user to enter a number.
--read the input, convert it to a float , and append it to number
After the loop , set largest = number[0]
for each num in numbers:
    if num > largest , update largest = num
    
    print the largest number
    END
    """

def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_vsl = num
        return max_val
def main():
    numbers = []
    for i in range(5):
        numbers.append(float(input(f"enter number {i + 1} :")))
        largest = find_max(numbers)
        print(f"the largest number is :{largest}")

if __name__ = "__main__"
    main()
