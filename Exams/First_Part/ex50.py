first_list = []
for i in range(20):
    number = int(input("Моля въведе3те число, което искате да "
                       "добавите в листа: "))
    first_list.append(number)
    print("Числото е добавено успешно!")

max_el = max(first_list)
min_el = min(first_list)
multiply = max_el * min_el
print(f"Произведението на минималния и максималния елемент "
      f"в листа е: {multiply}.")

count_bigger = 0
sum_of_el = 0
for number in first_list:
    sum_of_el += number
average = sum_of_el / len(first_list)
print(f"Средната стойност на числата в листа е: {average}")
for number in first_list:
    if number > average:
        count_bigger += 1
if count_bigger != 0:
    print("Броя на елементите в списъка, по-големи от "
          f"средноаритметичната стойност е: {count_bigger}.")
else:
    print("Няма елементи в списъка, по-големи от средноаритметичната стойност!")

second_list = []
for number in first_list:
    if number % 2 == 0:
        second_list.append(number)
        print(f"Успешно добавихте {number} в листа с числа!")

if len(second_list) > 0:
   max_el2 = max(second_list)
   sum_of_el2 = 0
   average2 = 0
   for number in second_list:
          sum_of_el2 += number
   average2 = sum_of_el2 / len(second_list)

   diff = abs(max_el2 - average2)
   print(f"Разликата между максималната и средноаритметичната стойност е: {diff}.")
   sum_of_first_last = second_list[0] + second_list[-1]
   second_list.append(sum_of_first_last)
   print(f"Добавихте сумата на първия и последния елемент от first_list {sum_of_first_last}, "
      f"към second_list!")
else:
    print("Листът е празен!")