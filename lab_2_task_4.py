n = int(input('Введите натуральное число:'))

n1 = n2 = 1
print(n1, n2, end=' ')

i = 1

while i < n:
    n1,n2 = n2, n1 + n2
    print(n2, end=' ')
    i += 1
