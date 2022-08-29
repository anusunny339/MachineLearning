print('21mca006')
print('Anu Sunny')

str=input("Enter a string:")

print(str)

vowels='aeiou'

print("count of vowels in the string:")

count={}.fromkeys(vowels,0)

for i in str:

   for j in count:

       if(i==j):

           count[j]=count[j]+1

print(count)

