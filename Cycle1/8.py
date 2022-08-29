
print('21mca006')
print('Anu Sunny')
num = int(input("Enter a 10 digit mobile number : "))
nums = []
for i in range(0, 10):
   n = num % 10
   nums.append(n)
   num = num // 10
print("numbers not in the mobile number are : ")
for i in range(0, 10):
   if i not in nums:
       print(i)
