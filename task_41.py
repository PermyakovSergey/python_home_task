# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

number = 8.98563
d = 0.001
count = 0
while d < 1:
    d *= 10
    count += 1
print(round(number, count))

# исходя из примера, к числу pi не применили функцию round(), round(pi, count) = 3.142,
# возможно ниже решение "правильнее"
# from cmath import pi
# print(round(pi, count))
not_round_num = int(number) + int((number % 1) * 10**count) / 10**count
print(not_round_num)