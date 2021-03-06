# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def calc_func(*args):
    sum = 0
    flag = False
    for i in args:
        try:
            if i:
                sum += float(i)
        except ValueError:
            flag = True
    return sum, flag

sum_all = 0

while True:
    numbers = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calc_func(*numbers)
    sum_all += sum
    print(f'сумма {sum_all}')

    if stop_flag:
        break