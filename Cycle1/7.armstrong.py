print('21mca006')
print('Anu Sunny')

for i in range(1,1000):
    temp=i
    sum=0
    while i > 0:
        r = i % 10
        sum = sum + (r * r * r)
        i= i // 10
    if sum == temp:
        print(temp)



