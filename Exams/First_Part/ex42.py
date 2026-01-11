import random

while True:
    n = int(input("Въведете число: "))
    if 20 < n < 40:
        print("Числото е в интервала!")
        break
    else:
        print("Въведи цяло число!")

my_list = []
for i in range(n):
    number = random.randint(2, 200)
    my_list.append(number) #добавяне на число

min_number = min(my_list) #минимална стойност
my_list.remove(min_number)
#remove - махаме по стойност
#pop - махаме по индекс

sum_of_numbers = 0
for idx in range(len(my_list)):
    if idx % 2 == 0: #намираме индекса
        current_element = my_list[idx] #намираме елемента на даден индекс
        sum_of_numbers += current_element

#list_1 = [1, 2, 3, 4]

count_of_num = 0
for number in my_list: #всяко число в листа
    last_digit = abs(number) % 10 #последната цифра - на единиците
    #last_digit = (abs(number) // 10) % 10 - на десетици
    #last_digit = (abs(number) // 100) % 10 - на стотици
    #last_digit = (abs(number) // 1000) % 10 - на хилядни
    if last_digit == 0:
        count_of_num += 1

second_list = []
for i in my_list:
    if i % 3 == 0 or i % 4 == 0:
        if i % 3 == 0 and i % 4 == 0:
            print("Не отговаря на условието")
        else:
            second_list.append(i)

average = 0
sum_of_number = 0
count_of_number = 0

for i in second_list: #25, 31, 27
    if i % 2 != 0:
        sum_of_number += i
        count_of_num += 1
average = sum_of_number/count_of_num

max_number = max(second_list)
index = second_list.index(max_number) #намираме индекса на даден елемент









