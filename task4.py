# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
S = int(input("Введите количесвтво журавликов, которые сделали дети"))
if S % 6 == 0:
    Kate = (S // 6) * 4
    Srgey =  S // 6
    Peter = S // 6
    print(F'Дети вместе сделали вместе {S} журавликов, {Kate} из которых сделала Катя, {Srgey} из которых сделал Сережа, {Peter} из которых сделал Петя')
else: print("Дети не могли сделать такое количество журавликов")
    


