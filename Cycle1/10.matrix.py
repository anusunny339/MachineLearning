print('21mca006')
print('Anu Sunny')

n=int(input("Enter the row size : "))
m=int(input("Enter the coloumn size : "))
a=[]
b=[]
c=[]
print("Enter the matrix - 1 : \n")
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        p=int(input())
        a[i].append(p)
print("Enter the matrix - 2 : \n")
for i in range(0,n):
    b.append([])
    for j in range(0,m):
        q=int(input())
        b[i].append(q)

c=[[0 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        c[i][j]=a[i][j]+b[i][j]
print("Matrix-1+Matrix-2")
for r in c:
    print(r)