score_list = []
for i in range(20):
    number = int(input("Въведете число, което искате да добавите в листа: "))
    score_list.append(number)

sum_of_numbers = 0
average = 0
for number in score_list:
    sum_of_numbers += number
if len(score_list) > 0:
   average = sum_of_numbers/len(score_list)
   print(f"Средната стойност на списъка е: {average}")
else:
    print("Листът е празен!")
count_numbers_greather_than_average = 0
for number in score_list:
    if number > average:
        count_numbers_greather_than_average += 1
if count_numbers_greather_than_average != 0:
    print(f"Броя на числата, които са по-големи от средната стойност на списъка"
          f" е: {count_numbers_greather_than_average}")
else:
    print("Няма числа, които да са по-големи от средната стойност на списъка!")

multiples_of_4 = []
for number in score_list:
    if number % 4 == 0:
        multiples_of_4.append(number)
        print(f"Добавихте числото {number} към multiplies_of_4.")

max_number = max(score_list)
sum_of_numbers_in_second_list = 0
average = 0
for number in multiples_of_4:
    sum_of_numbers_in_second_list += number
if len(multiples_of_4) > 0:
    average = sum_of_numbers_in_second_list/len(multiples_of_4)
    print(f"Средната стойност на списъка е: {average}")
    diff = max_number - average
    print(f"Разликата между най-голямото число в score_list и средната стойност "
          f"на multiples_of_4 e {diff}")
else:
    print("Листът е празен!")

first_element = score_list[0]
last_element = score_list[-1]
total = first_element + last_element
multiples_of_4.append(total)
print("Добавихте елемент към multiples_of_4, който е равен на сбора на първия "
      f"и последния елемент на score_list: {total}")

