number = int(input("Введите натуральное число: "))
prime_factors = []

for i in range(2, number+1):
    while number % i == 0:
        prime_factors += [i]
        number //= i
    if i*i > number:
        if number > 1:
            prime_factors += [number]
        break

print("Простые множители:", prime_factors)
