import random

while True:
  k = int(input("Въведете число в интервала (10 < k < 70)"))
  if 10 < k < 70:
     break
  else:
     print("Моля въведете число в посочения интервал!")

nums = []
r = random.randint(-4000, -1000)
s = random.randint(1000, 9000)

while len(nums) < k:
    number = int(input(f"Моля въведете число в интервала: {r} : {s} : "))
    if r < number < s:
        nums.append(number)
    else:
        print("Моля въведете число в зададения интервал!")

count_even_negative_del3 = 0
for number in nums:
    if number < 0 and number % 2 == 0:
        digit_of_hundreds = (abs(number) // 100) % 10
        if digit_of_hundreds % 3 == 0:
            count_even_negative_del3 += 1
if count_even_negative_del3 != 0:
    print("Броя на четните отрицателни елементи, с цифра на "
          f"стотиците кратна на 3 е {count_even_negative_del3}")
else:
    print("Няма четните отрицателни елементи, с цифра на "
          f"стотиците кратна на 3 в листа!")

nums2 = []
for number in nums:
    if number % 7 == 0:
        nums2.append(number)
        print(f"Добавихте {number} във втория лист.")

for idx in range(len(nums2)):
    if idx % 2 != 0:
        number_at_index = abs(nums2[idx])
        multiplication = 1
        while number_at_index > 0:
            digit = number_at_index % 10 #последната цифра на числото
            multiplication *= digit
            number_at_index = number_at_index // 10 #премахваме последната цифра
        nums2[idx] = multiplication #заменяме числото с резултата

if len(nums) == len(nums2):
    nums2 = list(reversed(nums2))
elif len(nums) > len(nums2):
    nums = nums[:-3]
elif len(nums2) > len(nums):
    nums2 = nums2[:-3]