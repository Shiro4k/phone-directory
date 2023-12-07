def print_all_contacts(file_name):
    with open(file_name, 'r', encoding='UTF8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end='\n\n')
        else:
            print('Список контактов пуст')

def connect_with_user():
    print('Введите <Фамилию> <Имя> <Телефон> (например: Иванов Иван 89*********): ')
    cont_info = str(input('---> '))
    return cont_info
def add_contact(file_name):
    with open(file_name, 'r', encoding='UTF8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='UTF8') as file:
        file.writelines(all_cont)

def find_contact(file_name):
    with open(file_name, 'r', encoding='UTF8') as file:
        all_cont = file.readlines()
    print('Выберите критерий для поиска:\
          \n 1 - Фамилия\
          \n 2 - Имя\
          \n 3 - Телефон\
          ')
    print('---> ', end='')
    comm = int(input())
    print()
    print('Введите строку для поиска :')
    data = input('---> ')
    print()
    print('Найденые контакты:')
    print('----------------')
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if cont_as_list[comm - 1] == data:
            print(*cont_as_list)
    print('----------------')

def delete_contact(file_name):
    with open(file_name, 'r', encoding='UTF8') as file:
        all_cont = file.readlines()
    print('Выберите критерий для Удаления:\
              \n 1 - Фамилия\
              \n 2 - Имя\
              \n 3 - Телефон\
              ')
    print('---> ', end='')
    comm = int(input())
    print()
    print('Введите строку для Удаления :')
    data = input('---> ')
    print()
    print('Найденые Совпадения:')
    user = list()
    index = 1
    print('----------------')
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if cont_as_list[comm - 1] == data:
            print(f'{index} {cont}', end='')
            user.append(cont.strip())
            index += 1
    print()
    print('----------------')
    print()
    print('Выберите контакт для Удаления')
    print('---> ', end='')
    num = int(input())
    print('Удаленные контакты:')
    print('----------------')
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if cont_as_list == user[num - 1].strip().split():
            print(*cont_as_list)
            all_cont.remove(cont)
    print('----------------')
    with open(file_name, 'w', encoding='UTF8') as file:
        file.writelines(all_cont)

def change_contact(file_name):
    with open(file_name, 'r', encoding='UTF8') as file:
        all_cont = file.readlines()
    print('Выберите критерий для поиска:\
              \n 1 - Фамилия\
              \n 2 - Имя\
              \n 3 - Телефон\
              ')
    print('---> ', end='')
    comm = int(input())
    print()
    print('Введите строку для поиска :')
    data = input('---> ')
    print()
    print('Найденые Совпадения:')
    user = list()
    index = 1
    print('----------------')
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if cont_as_list[comm - 1] == data:
            print(f'{index} {cont}')
            user.append(cont.strip())
            index += 1
    print('----------------')
    print()
    print('Выберите контакт для Изминения')
    num = int(input('---> '))
    print()
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if cont_as_list == user[num - 1].strip().split():
            ch_user = cont_as_list
            all_cont.remove(cont)
            print('Что хотите изменить:\
                \n 1 - Фамилия\
                \n 2 - Имя\
                \n 3 - Телефон\
                ')
            ch_num = int(input('---> '))
            print()
            if ch_num == 1:
                ch_user[0] = input('Введите новую фамилию:'+'\n'+'---> ')
            elif ch_num == 2:
                ch_user[1] = input('Введите новое имя:'+'\n'+'---> ')
            elif ch_num == 3:
                ch_user[2] = input('Введите новый телефон:'+'\n'+'---> ')
            else:
                print('Нет такого критерия')
            all_cont.append('\n' + ' '.join(ch_user))
    print('Контакт Изменен')
    with open(file_name, 'w', encoding='UTF8') as file:
        file.writelines(all_cont)