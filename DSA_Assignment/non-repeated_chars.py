

# Python implementation
from collections import Counter

 
 
def printNonrepeated(string):
 
    freq = Counter(string)
    # print(freq)

    for i in string:
        if(freq[i] == 1):
            print("First non-repeating character is " + i)
            break
 
 
string = input("Enter a String: ")
 
printNonrepeated(string)