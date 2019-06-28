documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "draft", "number": "13-7-4"},
    {"type": "The Book Of Heavy Metal", "number": "N-666"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': [],
    '13': ['13-7-4'],
    '666': ['N-666']
}

# TODO 1
#  Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#  p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
#  l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
#  s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
#  a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
#  Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

def add_document(docs, dirs):
    """
    (variable_1, variable_2, ...) -> variable_1, variable_2

    Adding new document and put this new document on shelf.

    :return:

    variable_1.append(new_dictionary)
    variable_2.update(str: list.append())

    """
    while True:
       type_d = str(input('\nВведите тип добавляемого документа: '))
       num_d = str(input('Введите номер документа: '))
       own_d = str(input('Введите владельца этого документа: '))
       num_dir = str(input('Введите номер полки: '))
       print(f'\nПроверьте правильность введенных данных:\n   тип документа - {type_d}\n   номер документа - {num_d}\n   владелец - {own_d}\n'
             f'   положить на полку №{num_dir}\n')
       yes_no = str(input('Данные введены верно? (да/д/yes/y, нет/н/no/n): '))
       if yes_no in ['да', 'yes', 'д', 'y']:
            docs.append({
                'type': type_d,
                'number': num_d,
                'name': own_d
            })
            if num_dir in dirs.keys():
                dirs[num_dir].append(num_d)
            else:
                dirs.update({num_dir: []})
                list(dirs[num_dir])
                dirs[num_dir].append(num_d)
            print('\n\nДокумент успешно добавлен!')
            break
       elif yes_no in ['нет', 'н', 'no', 'n']:
           print('\n\nВведем документ заново :)'.upper())
       else:
           print('\n\nТы вводиш какую-то абра-кадабру... Работа секретаря очень серьезная штука!'
                 '\n\nОшибок быть не должно!'
                 '\n\nСделай перерыв, а потом с новыми силами возвращайся к работе :)')
           break

# add_document()
# print(documents)
# print(directories)

def owner_documents(docs):
    """
    This function find owner of document.

    :param docs:
    hz
    :return:

    print owner

    """
    num_doc = str(input('\nВведите номер документа: '))
    lst = []
    for doc in docs:
        list(doc['number'])
        lst.append(doc['number'])
    if num_doc in lst:
        for doc in docs:
            if num_doc in doc['number']:
                try:
                    print('\nВладельцем документа №"{}" является {}'.format(num_doc, doc['name']))
                except KeyError:
                    print('\nУ документа №"{}" отсутствует владелец'.format(num_doc))
    else:
        print(f'\nДокумента под номером "{num_doc}" не существует. Проверьте правильность ввода и повторите попытку.')

# owner_documents(documents)
# print(documents)

def list_documents(docs):
    """
    Function for listing documents on shelf.

    :param docs:
    :return:
    print content variable with documents
    """
    print('\nНа текущий момент на наших полках присутствуют документы:\n')
    for doc in docs:
        try:
            print('{}{} "{}" "{}";'.format(' ' * 3, doc['type'], doc['number'], doc['name']))
        except KeyError:
            print('{}{} "{}" "НЕТ ВЛАДЕЛЬЦА";'.format(' ' * 3, doc['type'], doc['number']))

# list_documents(documents)

def number_shelf(dirs):
    """
    Search number shelf for document.

    :param dirs:
    :return:
    print number shelf
    """
    num_doc = str(input('\nВведите номер документа: '))
    list_num_doc = []
    for dir in dirs.items():
        for num in dir[1]:
            list_num_doc.append(num)
    if num_doc in list_num_doc:
        for dir in dirs.items():
            if num_doc in dir[1]:
                print(f'\nЭтот документ находится на {dir[0]} полке.')
                continue
    else:
        print(f'\nДокумента под номером "{num_doc}" на полках нет. Вы уверены, что такой документ есть?')

# print(directories.values())
# number_shelf(directories)


# TODO 2 Дополнительная (не обязательная)
#  d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
#  m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
#  as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
#  all - all - команда, которая выводит все документы и содержимое всех полок;

def delete_document(docs, dirs):
    """
    Delete document from list of documents and from shelf.

    :param docs:
    :param dirs:
    :return:
    change selfs and documents
    """
    num_doc = str(input('\nВведите номер удаляемого документа: '))
    # if doc in docs['']
    lst = []
    for doc in docs:
        list(doc['number'])
        lst.append(doc['number'])
    if num_doc in lst:
        for doc in docs:
            if num_doc in doc.values():
                docs.pop(docs.index(doc))
        for dir in dirs.items():
            if num_doc in dir[1]:
                dirs[dir[0]].remove(num_doc)
        print(f'\nДокумент под номером "{num_doc}" успешно удален.')
    else:
        print(f'\nДокумента под номером "{num_doc}" не существует. Проверьте правильность ввода и повторите попытку.\n')

# delete_document(documents, directories)
# print(documents)
# print(directories)

def move_document(dirs):
    """
    Move document to other shelf.
    :param dirs:
    :return:
    change shelfs
    """
    num_doc = str(input('\nВведите номер перемещаемого документа: '))
    num_dir = int(input('Введите номер новой полки (числовой формат от 1 до ...): '))
    num_dir = str(num_dir)
    list_num_doc = []
    for dir in dirs.items():
        for num in dir[1]:
            list_num_doc.append(num)
    if num_doc in list_num_doc:
        for dir in dirs.items():
            if (num_doc in dir[1]) and (num_dir in dirs.keys()):
                dirs[dir[0]].remove(num_doc)
                dirs[num_dir].append(num_doc)
                print(f'\nДокумент под номером "{num_doc}" успешно перемещен на полку №{num_dir}.')
                break
            elif (num_doc in dir[1]) and not(num_dir in dirs.keys()):
                dirs[dir[0]].remove(num_doc)
                dirs.update({num_dir: []})
                list(dirs[num_dir])
                dirs[num_dir].append(num_doc)
                print(f'\nДокумент под номером "{num_doc}" успешно перемещен на полку №{num_dir}.')
                break
            else:
                continue
    else:
        print(f'\nДокумента под номером "{num_doc}" нет на полках. '
                  'Проверьте правильность ввода и повторите попытку.')

# move_document(directories)
# print(directories)

def add_shelf(dirs):
    """
    Adding new shelf.

    :param dirs:
    :return:
    change shelfs
    """
    num_dir = input('\nВведите номер новой полки (числовой формат от 1 до ...): ')
    # num_dir = str(num_dir)
    if num_dir in dirs.keys():
        all_nums = str(dirs.keys())
        print(f'\nПолка с номером "{num_dir}" уже существует. В наличии имеются полки с номерами {all_nums[11:-2]}.')
        print(f'\nВыберите другой номер для новой полки и повторите попытку.'.upper())
    else:
        dirs.update({num_dir: []})
        print(f'\nПолка с номером "{num_dir}" успешно добавлена.')

# add_shelf(directories)
# print(directories)

def view_all_docs_and_dirs(docs, dirs):
    """
    View all documents and shelfs.

    :param docs:
    :param dirs:
    :return:

    print variable_1, variable_2

    """
    print('\nНа текущий момент на наших полках присутствуют документы:\n')

    for index, doc in enumerate(docs):
        try:
            print('{}{} Тип: {}, №"{}", владелец {};'.format(' ' * 3, index+1, doc['type'], doc['number'], doc['name']))
        except KeyError:
            print('{}{} Тип: {}, №"{}", владелец НЕТ ВЛАДЕЛЬЦА;'.format(' ' * 3, index+1, doc['type'], doc['number']))
    print('\nРасположение документов:\n')
    for dir in dirs:
        content = str(dirs[dir])
        print('{}Полка № {}: {}'.format(' ' * 3, dir, content[1:-1]))

# view_all_docs_and_dirs(documents,directories)
# print(directories)


# TODO 3 "Задача из занятия py_2-3"
#  Задача №3
#  Расширить домашние задание из лекции 1.4 «Функции — использование встроенных и создание собственных» новой функцией,
#  выводящей имена всех владельцев документов. С помощью исключения KeyError проверяйте, если поле "name" у документа.

def catch_exception(docs):
    """
    Show name all owners.

    :param docs:
    :return:
    """
    print(f'\n\nИмена всех владельцев всех документов:\n')
    for doc in docs:
        try:
            print(f'   * {doc["name"]}')
        except KeyError:
            print(f'   * {"Неверное заведение документа".upper()} № "{doc["number"]}". '
                  'Необходимо добавить поле "name": "НЕТ ВЛАДЕЛЬЦА"')

# catch_exception(documents)

def very_main():
    print('\n\nДобро пожаловать в мини программу секретаря Noname!'.upper())
    print('\n\nВам предоставляется почти безграничный функционал! Такого Вы нигде больше не увидите!'
          '\nДля удобства и простоты Вам достаточно ввести номер действия, чтобы программа выполнила нужное действие: '
          '\n\n   1. программа спросит номер документа и выведет имя человека, которому он принадлежит;'
          '\n   2. выведет список всех документов в формате: тип "номер" "владелец";'
          '\n   3. спросит номер документа и выведет номер полки, на которой он находится;'
          '\n   4. добавит новый документ в каталог и в перечень полок (будьте готовы ввести данные'
          ' о документе и полку, где хранить документ);'
          '\n   5. спросит номер документа и удалит его из каталога и из перечня полок;'
          '\n   6. спросит номер документа и целевую полку и переместит его с текущей полки на целевую;'
          '\n   7. спросит номер новой полки и добавит ее в перечень;'
          '\n   8. выводит все документы и содержимое всех полок;'
          '\n   X. NEW! выводит имена всех владельцев всех документов'
          '\n   9. вывод этой справки;'
          '\n\n   0. Выйти из программы.')
    while True:
        prog = str(input('\n=========================================================================================='
                         '\n\n  номер действия: '.upper()))
        if prog == '1':
            owner_documents(documents)
        elif prog == '2':
            list_documents(documents)
        elif prog == '3':
            number_shelf(directories)
        elif prog == '4':
            add_document(documents, directories)
        elif prog == '5':
            delete_document(documents, directories)
        elif prog == '6':
            move_document(directories)
        elif prog == '7':
            add_shelf(directories)
        elif prog == '8':
            view_all_docs_and_dirs(documents, directories)
        elif prog in ['x', 'X', 'x.', 'X.', 'х', 'Х', 'х.', 'Х.']:
            catch_exception(documents)
        elif prog == '9':
            print('\nДля удобства и простоты Вам достаточно ввести номер действия, '
                  'чтобы программа выполнила нужное действие: '
                  '\n\n   1. программа спросит номер документа и выведет имя человека, которому он принадлежит;'
                  '\n   2. выведет список всех документов в формате: тип "номер" "владелец";'
                  '\n   3. спросит номер документа и выведет номер полки, на которой он находится;'
                  '\n   4. добавит новый документ в каталог и в перечень полок (будьте готовы ввести данные'
                  ' о документе и полку, где хранить документ);'
                  '\n   5. спросит номер документа и удалит его из каталога и из перечня полок;'
                  '\n   6. спросит номер документа и целевую полку и переместит его с текущей полки на целевую;'
                  '\n   7. спросит номер новой полки и добавит ее в перечень;'
                  '\n   8. выводит все документы и содержимое всех полок;'
                  '\n   x. NEW! выводит имена всех владельцев всех документов'
                  '\n   9. вывод этой справки;'
                  '\n\n   0. Выйти из программы.')
        elif prog in ['0', 'o', 'O']:
            print('\n   Надеемся Вам очень понравилась наша программа!',
                  '\n   Вопросы и предложения присылайте по адресу: info@it-vi.ru',
                  '\n   Досвидания!'.upper())
            break
        else:
            print('\nТакой функционал программы пока не подвезли)))'
                  '\nЕсть предложения? Пишите по адресу: info@it-vi.ru')

if __name__ == '__main__':
    very_main()

