def findPair(lst, n, target):
    for i in range(n-1):
        for j in range(1,n):
            if (lst[i] + lst[j] == target):
                print("Pair found " "(", lst[i] ,",", lst[j],")")
print("Pair not found")

n=int(input("Enter the range of number list: "))
lst=[]
for i in range(n):
    element=int(input("Enter the element for a list: "))
    lst.append(element)

target = int(input("Enter the target to find the pairs of an integer number: "))
 


findPair(lst, n, target)
 