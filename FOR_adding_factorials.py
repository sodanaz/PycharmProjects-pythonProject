j = int(input())
summ = 0
fact = 1
for i in range(1,j+1):
    fact = fact*i
    summ+=fact
print(summ)