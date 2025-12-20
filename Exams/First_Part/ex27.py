prices = []
for i in range(20):
    number = int(input("Въведете число, което искате да добавите в листа: "))
    prices.append(number)

max_number = max(prices)
min_number = min(prices)
total = min_number * max_number
print(f"Произведението на максималната и минималната стойност е: {total}")

count_odd_prices = 0
for price in prices:
    if price % 2 != 0:
        count_odd_prices += 1
if count_odd_prices != 0:
    print(f"Броя на цените, които са нечетни числа е: {count_odd_prices}")
else:
    print("Няма цени в листа, които да са нечетни числа!")

discounted_prices = []
for price in prices:
    if price % 10 == 0:
        discounted_prices.append(price)
        print(f"Добавихте {price} към втория лист.")

sum_of_numbers = 0
average = 0
for price in discounted_prices:
    sum_of_numbers += price
if len(discounted_prices) > 0:
    average = sum_of_numbers / len(discounted_prices)
    print(f"Средната стойност на discounted_prices е: {average}")
else:
    print("Списъка discounted_prices е празен!")

diff = max_number - average
print("Изчислете разликата между най-голямата цена"
      f"от prices и средната стойност на discounted_prices е: {diff}.")

first_element = prices[0]
last_element = prices[-1]
total = first_element + last_element
print(f"Сумата на първия и последния елемент на prices e: {total}")
discounted_prices.append(total)
print("Добавихте сумата към листа discounted_prices.")