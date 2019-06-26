# Задача №1
# Нужно реализовать Польскую нотацию для двух положительных чисел. Реализовать нужно будет следующие операции:
#
# Сложение
# Вычитание
# Умножение
# Деление
# Например, пользователь вводит: + 2 2 Ответ должен быть: 4
#
# Задача №2
# С помощью выражения assert проверять, что первая операция в списке доступных операций (+, -, *, /). С помощью конструкций try/expcept ловить ошибки и выводить предупреждения Типы ошибок:
#
# Деление на 0
# Деление строк
# Передано необходимое количество аргументов
# и тд.


# def prefix_notation():
#     operator = input('Введите арифметический оператор (+ - * /): ')
#     operand_1 = int(input('Введите первый операнд: '))
#     operand_2 = int(input('Введите второй операнд: '))
#     int(operand_1)
#     int(operand_2)
#     # result = operand_1 + operator + operand_2
#     # print(result)
#     print(operand_1, operator, operand_2, sep='')
#     print(4+1)
#     print(operator)
#     print(type(operator))
#     print('================================')
#     print(operand_1)
#     print(type(operand_1))
#     print('================================')
#     print(operand_2)
#     print(type(operand_2))
#     print('================================')

try:
    def summ(a, b):
        return int(a) + int(b)

    def sub(a, b):
        return int(a) - int(b)

    def mul(a, b):
        return int(a) * int(b)

    def div(a, b):
        return int(a) / int(b)
except ValueError as err:
    print('Неверный ввод. Обратите внимание на то, что Вы вводите.\n'
          'Детально: ', err)

func = {'+':summ, '-':sub, '*':mul, '/':div}
oper = ['+', '-', '*', '/']
result = None

def prefix_notation():
    try:
        a, b, c = input('Введите оператор и операнды через пробел (напр., + 1 2): ').split()
    except ValueError as err:
        print('\nНеверный ввод. Обратите внимание на то, что Вы вводите.\n'
              'Детально: ', err)
    else:
        try:
            if a in oper:
                result = func[a](b,c).__round__(2)
                print(f'\nВ итоге выражение "{a} {b} {c}" дало "{result}".'
                      f'\nВ привычном виде это выглядит так: {b} {a} {c} = {result}')
        except ZeroDivisionError as err:
            print('Плохая идея делить на 0 :))\n'
                  'Детально: ', err)
        except ValueError as err:
            print('Неверный ввод. Обратите внимание на то, что Вы вводите.\n'
                  'Детально: ', err)
        except UnboundLocalError as err:
            print('Неверный ввод. Обратите внимание на то, что Вы вводите.\n'
                  'Скорее всего недостаточно аргументов.\n'
                  'Детально: ', err)
    # elif:
    # print(a)
    # print(b)
    # print(c)
    # print(result)
    # return x


prefix_notation()










def very_main():
    print('\n\nДобро пожаловать в мини-реализацию Польской нотации!'.upper())
    print('\n\nВам необходимо ввести номер действия, чтобы программа выполнила нужное действие: '
          '\n\n   1. Польская (префиксная) нотация. Программа попросит ввести оператор и числа.'
          '\n\n   0. Выйти из программы.')
    while True:
        prog = str(input('\n=========================================================================================='
                         '\n\n  номер действия: '.upper()))
        if prog == '1':
            prefix_notation()
        # elif prog == '2':
        #     list_documents(documents)
        # elif prog == '3':
        #     number_shelf(directories)
        elif prog == '0':
            print('\n   Надеемся Вам очень понравилась наша программа!',
                  '\n   Вопросы и предложения присылайте по адресу: info@it-vi.ru',
                  '\n   Досвидания!'.upper())
            break
        else:
            print('\nТакой функционал программы пока не подвезли)))'
                  '\nЕсть предложения? Пишите по адресу: info@it-vi.ru')

# if __name__ == '__main__':
#     very_main()