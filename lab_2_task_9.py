number = int(input("Введите число: "))
reverse_number = 0

while number > 0:
    last_digit = number % 10
    reverse_number = reverse_number * 10 + last_digit
    number //= 10

print("Обратное число:", reverse_number)
