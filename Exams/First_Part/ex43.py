import random
import sys
while True:
    try:
        n = int(input("Въведете число в интервала (25<=n<= 45): "))
        if 25 <= n <= 45:
            print("Числото е в интервала!")
            break
        else:
            print("Моля въвдете число в посочения интервал!")
    except ValueError:
        print("Моля въведете валидни данни!")

list_1 = []
p = random.randint(-3700, -1600) #nqkvo random chislo
q = random.randint(2222, 3333) #nqkvo random chislo

while len(list_1) < n:
    number = int(input(f"Въведете число в интервала {p}:{q}: "))
    if p < number < q:
        print("Отговаря на условието!")
        list_1.append(number) #list - dobawqne - chislo
    else:
        print("Моля въведете число в интервала!")

#for i in range(n): n = 5
#    number = int(input(f"Въведете число в интервала {p}:{q}: "))
#    number = random.randint(p, q)
#    if p < number < q:
#        print("Отговаря на условието!")
#        list_1.append(number) #list - dobawqne - chislo
#    else:
#        print("Числото не е в интервала!")

count_positive_elements = 0
for number in list_1:
    if number > 0:
        print("Числото е положително!")
        digit_ot_hundreds = (abs(number) // 100) % 10
        if digit_ot_hundreds % 2 == 0:
            count_positive_elements += 1
if count_positive_elements != 0:
    print("Броя на ....... е .....")
else:
    print("Няма положително кратни......")

min_element = sys.maxsize #9054824791034930480275
for idx in range(len(list_1)):
    current_element = list_1[idx]
    if idx % 6 == 3:
        if current_element < min_element:
            min_element = current_element
idx = list_1.index(min_element)
print(f"Индекса на елемента с най-малка стойност е: {idx}.")

list_2 = []
for number in list_1:
    if 10 <= abs(number) <= 99 and number % 5 == 0:
        list_2.append(number)

multiply = 1
for idx in range(len(list_2)):
    if idx % 2 != 0:
        current_element = list_2[idx] #имаме индекса - търсим елемента
        #current_index = list_2.index(current_element) имаме елемента - търсим индекса
        multiply *= current_element

for idx in range(len(list_2)):
    if idx % 2 != 0:
        current_element = list_2[idx]
        if current_element % 2 == 0:
            list_2.remove(list_2[idx])

if len(list_1) < len(list_2):
    mid_element = len(list_1) // 2
    first_element = list_1[0]
    last_element = list_1[-1]
    new_element = first_element + last_element
    list_1.insert(mid_element, new_element)
elif len(list_2) < len(list_1):
    mid_element = len(list_2) // 2
    first_element = list_2[0]
    last_element = list_2[-1]
    new_element = first_element + last_element
    list_2.insert(mid_element, new_element)








