"""
ALGORITHM
START
prompt the user t enter a single letter 
read the input and store it as a string 
convert the letter to lowercase for case-insensetive comparision
check if the letter is in the set of vowel {'a','e','i','o','u'}
if true ,print "vowel"
else , print "consonant"
END
"""

def is_vowel(ch):
    return ch.lower() in {'a','e','i','o','u'}

def main():
    letter = input("enter a single leter:")
    if is_vowel(letter):
        print("vowel")
    else:
        print("consonent")



if __name__ == "__main__" :
    main()