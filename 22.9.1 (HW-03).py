numbers = list(map(int, input("Введите числа через пробел: ").split()))
number = int(input("Введите число для поиска: "))

position = -1
for i, n in enumerate(numbers):
    if n == number:
        position = i
        break
if position == -1:
    print("Число не найдено")
else:
    print("Число найдено на позиции", position)