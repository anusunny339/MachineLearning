#21MCA006
#Anu Sunny

print('21mca006')
print('Anu Sunny')
def bubFunc(a, val):
   for i in range(val -1):
       for j in range(val - i - 1):
           if(a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

a = []
val = int(input("Please Enter the Total Elements : "))
for i in range(val):
   value = int(input("Please enter the %d Element : " %i))
   a.append(value)

bubFunc(a, val)
print("The List in Ascending Order : ", a)
