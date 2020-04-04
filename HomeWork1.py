# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
# чисел и строк и сохраните в переменные, выведите на экран.

a = 123
b = "abc"
print(a)  # int
print(b)  # str
c = input('Ведите число: ')
print(c)  # str
print(int(c))  # int
d = input('Ведите текст: ')
print(d)  # str


# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Введите время в секундах: "))

h = time // 3600
if h < 10:
    h = "0" + str(h)
m = (time % 3600) // 60
if m < 10:
    m = "0" + str(m)
s = (time % 3600) % 60
if s < 10:
    s = "0" + str(s)
print(f'Введённое время в часовом формате: {h}:{m}:{s}')


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Введите число: ")
result = int(n) + int(n+n) + int(n+n+n)
print(f'Сумма чисел {n}, {n+n} и {n+n+n} = {result}')


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = input('Введите целое положительно число: ')

while float(user_number) % 1 != 0 or float(user_number) < 0:  # проверка введённого числа
    user_number = input('Вы ввели некорректное число. Введите целое положительно число: ')

last_digit = int(user_number) % 10
user_number = int(user_number) // 10
result = 0
while user_number or last_digit:
    if last_digit > 8:
        result = last_digit
        break
    elif last_digit > result:
        result = last_digit
    last_digit = user_number % 10
    user_number = user_number // 10

print('Наибольшее число ', result)