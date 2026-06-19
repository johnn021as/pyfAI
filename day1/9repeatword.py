"""Algorithm
START 
define a function repeat(wrd,times) that takes two parameters : a string word and an integer times
---inside the function :
-initialise an empty string result =""
-for i from 1 to times(inclusive)
    concatenate word to result
return result
---outside the function 
-call repeat() with sample arguments and print the result.

END """


def repeat(word, times):
    result = " "
    for _ in range(times)
        result += word

    return result

def main():
    w = input("enter a word:")
    t = int(input("enter number of repetions:"))
    print(repeat(w,t))

if __name__ == "__main__" :
    main()
    