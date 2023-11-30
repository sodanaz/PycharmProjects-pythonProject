'''some_set = {1,'python', 3, 3, 3, 14, 14, 'door'}
print(some_set)'''


# to input as many things as you want use input().split()
'''the code below allows you to enter as many elements as 
you want. 'some_array' variable will store your data in 
a !list! type of data structure. All elements of this list are 
string type by default'''

some_array = input('input numbers, please: ').split()


'''the code below will convert elements from string type into
integer type'''
for i in range(len(some_array)):
    some_array[i] = int(some_array[i])

been_before = []
for i in some_array:
    if i in been_before:
        print('YES')
    else:
        print('NO')
        been_before.append(i)












