temperatures = []
for i in range(30):
    number = int(input("Въведете число, което ще добавите в листа: "))
    temperatures.append(number)
    print(f"Добавихте числото {number}.")

sum_positive_tem = 0
sum_negative_tem = 0
for temp in temperatures:
    if temp < 0:
        sum_negative_tem += temp
    else:
        sum_positive_tem += temp
if sum_negative_tem != 0:
    print(f"Сумата на отрицателните температури е: {sum_negative_tem}.")
else:
    print("Няма отрицателни температури в листа!")
if sum_positive_tem != 0:
    print(f"Сумата на положителните температури е: {sum_positive_tem}.")
else:
    print("Няма положителни температури в листа!")

count_del7 = 0
for temp in temperatures:
    if abs(temp) % 7 == 0:
        count_del7 += 1
if count_del7 != 0:
    print(f"Броя на елементите, които са кратни на 7 е: {count_del7}")
else:
    print("Няма елементи, кратни на 7 е листа!")

above_average = []
sum_elements = 0
average = 0
for temp in temperatures:
    sum_elements += temp
if len(temperatures) > 0:
    average = sum_elements/len(temperatures)
    print(f"Средната стойност на първия списък е: {average}")
else:
    print("Листа е празен!")

for temp in temperatures:
    if temp > average:
        above_average.append(temp)
        print(f"Добавихте {temp} към втория лист.")

max_element = max(temperatures)
min_element = min(temperatures)
diff = max_element - min_element
above_average.append(diff)
print("Добавихте към above_average нов елемент, равен на разликата"
      f" между максималната и минималната стойност в temperatures: {diff}.")