first_list = []
for i in range(25):
    number = int(input("Въведете число, което искате да добавите в листа!"))
    first_list.append(number)
    print("Числото беше успешно добавено!")

sum_odd_el = 0
for number in first_list:
    if number % 2 != 0:
        sum_odd_el += number
if sum_odd_el != 0:
    print(f"Сумата на всички нечетни елементи е: {sum_odd_el}.")
else:
    print("Няма нечетни елеменгти в листа!")

count_el_less_av = 0
sum_of_el = 0
average = 0
for number in first_list:
    sum_of_el += number
average = sum_of_el / len(first_list)
for number in first_list:
    if number < average:
        count_el_less_av += 1
if count_el_less_av != 0:
    print("Броя на елементите, по-малки от средната стойност на листа"
          f"е: {count_el_less_av}.")
else:
    print("Няма елементи, по-малки от средната стойност на списъка!")

second_list = []
for number in first_list:
    if number % 4 == 0:
        second_list.append(number)
        print(f"Успешно добавихте числото {number} във втория лист!")

if len(second_list) > 0:
    min_el = min(second_list)
    sum_of_all_el = 0
    average = 0
    for number in second_list:
        sum_of_all_el += number
    average = sum_of_all_el / len(second_list)
    print(f"Средноаритметичната стойност на елементите"
          f"от втория лист е: {average}.")

    diff = abs(min_el - average)
    print("Разликата между минималния елемент и "
          f"средноаритметичната стойност е: {diff}.")

    sum_first_last_el = second_list[0] + second_list[-1]
    second_list.append(sum_first_last_el)
    print(f"Добавихте числото {sum_first_last_el} към втория списък!")

else:
    print("Няма числа, кратни на 4 в first_list!")
    print("Втория лист 'second_list' в празен!")