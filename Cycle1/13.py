
print('21mca006')
print('Anu Sunny')
num=int(input("enter the number"));
temp=num
while temp>0:
    num=temp
    sum=0
    while num > 0:
        d = num % 10
        sum = sum + d
        num = num // 10

    print("{} - {} = ".format(temp,sum),end="")
    temp=temp-sum
    print(temp)



