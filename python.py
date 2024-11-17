num = 5 
# output = 1+2+3+4+5 = 15
sum = 0

for i in range(num+1):
    sum += i
print(sum)


num1, num2 = 3, 6
sum = 0
for i in range(num1,num2+1):
  sum+=i
print(sum)

num1, num2 = 4, 2

if num1 > num2 :
    print(f'{num1} is greater')
else:
    print(f'{num2} is greater')