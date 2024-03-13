'''

Вася решил заняться торговлей рыбой. С помощью методов машинного обучения он предсказал цены на рыбу на N дней вперёд. Он решил, что в один день он купит рыбу, а в один из следующих дней — продаст (то есть совершит или ровно одну покупку и продажу или вообще не совершит покупок и продаж, если это не принесёт ему прибыли). К сожалению, рыба — товар скоропортящийся и разница между номером дня продажи и номером дня покупки не должна превышать K.

Определите, какую максимальную прибыль получит Вася.

Формат ввода
В первой строке входных данных задаются числа N и K (1 ≤ N ≤ 10000, 1 ≤ K ≤ 100).

Во второй строке задаются цены на рыбу в каждый из N дней. Цена — целое число, которое может находится в пределах от 1 до 109.

Формат вывода
Выведите одно число — максимальную прибыль, которую получит Вася.

Пример 1
Ввод
5 2
1 2 3 4 5

Вывод
2
Пример 2
Ввод
5 2
5 4 3 2 1

Вывод
0

'''

print('----XXXXXXXXXXXXXXXX---\n')

n = 5
k = 2
prices = [1, 2, 3, 4, 5]

# n = 5
# k = 2
# prices = [5, 4, 3, 2, 1]

# n = 10
# k = 10
# prices = [6, 7, 5, 5, 10, 10, 1, 8, 5, 10]

prices.reverse()

value = 0
max_value = 0


# if n - k == 0:
#     r = n


for i in range(n):

    price_slice = prices[i:i + k + 1]
    print(price_slice)

    right_price = max(price_slice)
    print('RIGHT PART:', right_price)

    right_price_index = price_slice.index(right_price)
    print('INDEX:', right_price_index)
    print(price_slice[right_price_index:])

    left_price = min(price_slice[right_price_index:])
    print('LEFT PART:', left_price)

    value = right_price - left_price
    print(f'\n{value} = {right_price} - {left_price}\n')
    if value > max_value:
        max_value = value



print(f'\n\tANSWER: {max_value}')



print('\n\n\n-------------DONE----------------\n')

#
# n = 5
# k = 2
# prices = [5, 4, 3, 2, 1]

n, k = map(int, input().split())
prices = list(map(int, input().split()))

prices.reverse()

value = 0
max_value = 0

for i in range(n):
    price_slice = prices[i:i + k + 1]
    right_price = max(price_slice)
    right_price_index = price_slice.index(right_price)
    left_price = min(price_slice[right_price_index:])
    value = right_price - left_price

    if value > max_value:
        max_value = value

print(max_value)

