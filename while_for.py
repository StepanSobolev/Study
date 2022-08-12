changes = input('Введите число: ')
count = 1
for_sum = 0

for i in range(1, int(changes) + 1):
    if i % 3 != 0:
        for_sum += i ** 3
print(for_sum)

# ___________________________________________

while_sum = 0
while count <= int(changes):
    if count % 3 != 0:
        while_sum += count ** 3
    count += 1

print(while_sum)
