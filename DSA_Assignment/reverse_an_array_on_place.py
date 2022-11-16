
def reverseList(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

 

n=int(input("Enter the range of number list: "))
lst=[]
for i in range(n):
    element=int(input("Enter the element for a list: "))
    lst.append(element)
    
reverseList(lst,0,n-1)
print("Reversed list is")
print(lst)
