changes = input('Введите число: ')
print(changes)
count = 1

for i in range(1, int(changes)+1):
    if i % 3 != 0:
        print(i ** 3, end=', ')
print()

while count <= int(changes):
    if count % 3 != 0:
        print(count ** 3, end=', ')
    count += 1