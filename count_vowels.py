# Количество гласных

text = input("Введите строку: ").lower()
vowels = "аеёиоуыэюя"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Количество гласных:", count)
