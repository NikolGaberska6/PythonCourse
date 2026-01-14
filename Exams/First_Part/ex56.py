import random

numbers = []
for i in range(25):
    number = random.randint(1, 100)
    numbers.append(number)
    print(f"Успешно добавихте числото {number} в листа!")

min_el = min(numbers)
print(f"Минималния елемент в листа е: {min_el}")

sum_el_greater_50 = 0
for number in numbers:
    if number > 50:
        sum_el_greater_50 += number
if sum_el_greater_50 != 0:
    print(f"Сумата на всички елементи, по-големи от 50 е: {sum_el_greater_50}.")
else:
    print("Няма елементи в листа, по-големи от 50.")

odd_numbers = []
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
        print(f"Успешно добавихте числото {number} в листа!")

if len(odd_numbers) > 0:
    leng = len(odd_numbers)
    print(f"Дължината на втория списък е: {leng}.")

    middle_element = len(odd_numbers) // 2
    odd_numbers.pop(middle_element)
    print("Изтрихте средния елемент от втория лист 'odd_numbers'.")

else:
    print("Няма нечетни числа в първия лист!")
    print("Втория лист е празен!")
    