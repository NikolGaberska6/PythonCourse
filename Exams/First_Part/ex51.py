numbers_list = []
for i in range(30):
    number = int(input("Въведете число, което искате да добавите в листа!"))
    numbers_list.append(number)
    print(f"Числото {number} бе добавено успешно в листа!")

sug_neg_nums = 0
for number in numbers_list:
    if number < 0:
        sug_neg_nums += number
if sug_neg_nums != 0:
    print(f"Сумата на всички отрицателни елементи е: {sug_neg_nums}.")
else:
    print("Няма отрицателни елементи в листа!")

count_del3 = 0
for number in numbers_list:
    if number % 3 == 0:
        count_del3 += 1
if count_del3 != 0:
    print(f"Броя на елементите, които са кратни на 3 е: {count_del3}.")
else:
    print("Няма елементи в листа, които да са кратни на 3!")

filtered_list = []
for number in numbers_list:
    if number > 0 and number % 2 == 0:
        filtered_list.append(number)
        print(f"Успешно добавихте числото {number} в списъка с числа filtered_list!")

if len(filtered_list) > 0:
    max_el = max(filtered_list)
    print("Максималната стойност на елементите от втория списък "
          f"е: {max_el}.")

    average = 0
    sum_of_el = 0
    for number in filtered_list:
        sum_of_el += number
    average = sum_of_el / len(filtered_list)
    print(f"Средната стойност на елементите във filtered е: {average}.")
    filtered_list.append(average)
    print(f"Успешно добавихте числото {average} към втория лист filtered_list!")

else:
    print("Вторият лист filtered_list е празен!")