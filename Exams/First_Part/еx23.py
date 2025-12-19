
data_list = []
for i in range(25):
    number = int(input("Въведете число: "))
    data_list.append(number)
    print("Добавихте числото в листа.")

max_element = max(data_list)
min_element = min(data_list)
diff = max_element - min_element
print(f"Разликата между максималната и "
      f"минималната стойност в списъка е {diff}")

count_negative_nums = 0
for number in data_list:
    if number < 0:
        count_negative_nums += 1
if count_negative_nums != 0:
    print(f"Броя на отрицателните числа в списъка е {count_negative_nums}")
else:
    print("Няма отрицателни числа в списъка!")

even_list = []
for number in data_list:
    if number % 2 == 0:
        even_list.append(number)
        print(f"Добавихте {number} към списъка с числа.")

average = sum(data_list[:3])/3
print(f"Средната стойност на първите три елемента от data_list e {average}")

sum_of_elements = 0
for number in even_list:
    sum_of_elements += number

full_sum = sum_of_elements + average
print("Сумата на елементите в even_list и средната стойност "
      f"на първите три елемента от data_list е {full_sum}")

sum_max_min_elements = max_element + min_element
even_list.append(sum_max_min_elements)
print(f"Добавихте {sum_max_min_elements} към листа.")
