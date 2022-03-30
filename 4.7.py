def fact(n):
    count = 1
    n = int(input('Enter number: '))
    while count <= n:
        yield count
        count += 1
i = 1
my_list = []
for el in fact(n):
    if i > n:
        break
    else:
        my_list.append(el)
        i += 1
print(my_list)
