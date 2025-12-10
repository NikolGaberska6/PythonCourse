from operator import index
mylst1 = []
is_true = True
number_count = 0

while True:
 try:
    n = int(input("Въведете броя на числата в списъка - между 10 и 50: "))
    if 10 <= n <= 50:
        break
    else:
        print("Моля въедете число в дадения интервал!")

 except:
    print("Грешка! Моля, въведете валидно число.")


number1 = int(input("Въведете число в интервала -2500, -1300: "))
if -2500 <= number1 <= -1300:
    first_cond = number1
number2 = int(input("Въведи число в интервала: 1111, 4444: "))
if 1111 <= number2 <= 4444:
    second_cond = number2

while is_true:
    nums_for_list = int(input(f"Въведете число в интервала {number1}, {number2}: "))
    if number1 <= nums_for_list <= number2:
        number_count += 1
        mylst1.append(nums_for_list)
    else:
        print("Моля въведете число в дадения интервал!")
    if number_count >= n:
        is_true = False
print(mylst1)

count_negative_nums = 0
for num in mylst1:
    if num < 0:
        if ((num // 10) % 10) % 4 == 0 or ((num // 10) % 10) % 5 == 0:
         count_negative_nums += 1

sum_of_indexex = 0
nums_for_average = []
sum_for_average = 0
for element in mylst1:
    element = str(element)
    for idx in element:
        idx = int(idx)
        sum_of_indexex += idx
    if 10 <= sum_of_indexex <= 99 and sum_of_indexex % 2 == 0:
        element = int(element)
        nums_for_average.append(element)
        sum_for_average += element
    sum_of_indexex = 0

average = sum_for_average / len(nums_for_average)
print(average)

mylist2 = []
sum_of_index = 0
num_odd_elements = 0
for numbers in mylist2:
    if 100 <= numbers <= 999 and numbers % 3 == 0:
      mylist2.append(numbers)
    numbers = str(numbers)
    for idx in numbers:
        numbers = int(numbers)
        sum_of_index += idx
    index = mylist2.index(numbers)
    if index % 2 == 0 and sum_of_index % 2 != 0:
        num_odd_elements += 1
    elif index % 2 != 0:
        mylist2.pop(index)
        mylist2.insert(index, 13)
    sum_of_index = 0

print(num_odd_elements)

first_length = len(mylst1)
second_length = len(mylist2)

if first_length > second_length:
    mylst1.pop(0)
    mylst1.pop(len(mylst1)-1)
else:
    mylist2.pop(0)
    mylist2.pop(len(mylist2)-1)

print(mylst1)
print(mylist2)
