print('21mca006')
print('Anu Sunny')

n1=int(input("enter the size of list1"))
list1=[]
print("enter the elements")
for i in range(0,n1):
    ele=int(input())
    list1.append(ele)

n2=int(input("enter the size of list2"))
list2=[]
print("enter the elements")
for i in range(0,n2):
    ele=int(input())
    list2.append(ele)
print(list1)
print(list2)
list3=[]
if n1 == n2:
    print("added list")
    for i in range(0,n1):
        ele=list1[i]+list2[i]
        list3.append(ele)
    print(list3)
else:
    print("lists are of different size,addition not possible")
