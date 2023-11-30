line_num = int(input())
words = set()

for i in range(line_num):
    a = input().split()
    words.update(a)
print(len(words))

