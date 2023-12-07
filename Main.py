import Function
f = Function
CONTACTS = 'Contacts.txt'

def interface():
    while True:
        print('Выберете действие:\
         \n 1 - Добавить контакт \
         \n 2 - Вывести все контакты\
         \n 3 - Найти контакт\
         \n 4 - Изминить контакт\
         \n 5 - Удалить контакт\
         \n 0 - Выход')
        command = int(input('---> '))
        print()
        match command:
            case 0:
                break
            case 1:
                f.add_contact(CONTACTS)
            case 2:
                f.print_all_contacts(CONTACTS)
            case 3:
                f.find_contact(CONTACTS)
            case 4:
                f.change_contact(CONTACTS)
            case 5:
                f.delete_contact(CONTACTS)
            case _:
                print('Неверная команда!!!')
        print()

if __name__ == '__main__':
    interface()