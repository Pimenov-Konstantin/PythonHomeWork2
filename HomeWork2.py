# 1. Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
print(' Задача 1 ')
n_list = [1,2,3,4,5]

def sum_x(t_list):
    l_list = len(t_list)
    r_sum = 0  
    for i in range(0,l_list,2):
        r_sum += t_list[i]
    return r_sum
    
print(f'Сумма чисел списка {n_list} стоящих на нечетной позиции - {sum_x(n_list)}')

# 3. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
print(' Задача 2 ')
a_list = [2, 3, 4, 5, 6]
def para(b_list):
    kolvo_par = len(b_list)//2+len(b_list)%2
    c_list = []
    for i in range(0,kolvo_par):
        c_list.append(b_list[i] * b_list[-(i+1)])
    return c_list

print(f' Исходные данные - {a_list}')
print(f' Произведение пар в списке - {para(a_list)}')

# 4. Написать программу преобразования десятичного числа в двоичное
print(' Задача 4 ')
def des(a):
    dv = ''
    while a > 0:
        dv =str(a % 2) + dv
        a = a //2
    return dv
b = 250
print(f'Десятичное число {b} в двоичной записи {des(b)}')
