# Функция, считывающая контакты из файла data.txt, используя кодировку windows-1251
def read_contacts():
    try:
        with open('data.txt', 'r', encoding = 'windows-1251') as f:
            contacts = f.readlines()
            return [contact.strip() for contact in contacts]
    except FileNotFoundError:
        return []

# Функция, записывающая все контакты из переданного списка contacts
def write_contacts(contacts):
    with open('data.txt', 'w') as f:
        for contact in contacts:
            f.write(contact + '\n')

# Функция, демонстирирующая все контакты
def show_all_contacts():
    contacts = read_contacts()
    if contacts:
        for contact in contacts:
            print(contact)
        print()
    else:
        print('***Телефонная книга пуста***')
        print()

# Функция, реализующая поиск контактов
def find_contact():
    contacts = read_contacts()
    name = input('Введите имя: ')
    for contact in contacts:
        if name in contact:
            print(contact)
    print()

# Функция, добавляющая новые контакты
def add_contact():
    name = input('Введите имя и фамилию: ')
    phone_number = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new_contact = f'{name}: {phone_number} | комментарий: {comment}'
    contacts = read_contacts()
    contacts.append(new_contact)
    write_contacts(contacts)

# Функция, которая изменяет существующий контакт
def update_contact():
    name = input('Введите имя и фамилию: ')
    phone_number = input('Введите новый номер телефона: ')
    comment = input('Введите комментарий: ')
    contacts = read_contacts()
    for i in range(len(contacts)):
        if name in contacts[i]:
            contacts[i] = f'{name}: {phone_number} | комментарий: {comment}'
            write_contacts(contacts)
            break
    else:
        print('***Контакт не найден***')

# Функция, удаляющая контакты
def delete_contact():
    name = input('Введите имя: ')
    contacts = read_contacts()
    for i in range(len(contacts)):
        if name in contacts[i]:
            del contacts[i]
            write_contacts(contacts)
            break
    else:
        print('***Контакт не найден***')

# Функция для вывода главного меню справочника
def main():
    contacts = read_contacts()
    while True:
        print('Команды для работы со справочником:')
        print('1. Открыть файл телефонной книги')
        print('2. Сохранить файл телефонной книги')
        print('3. Показать все контакты')
        print('4. Найти контакт')
        print('5. Добавить контакт')
        print('6. Изменить контакт')
        print('7. Удалить контакт')
        print('8. Выход')
        choice = input('введите команду > ')
        if choice == '1':
            read_contacts()
            print('***Файл телефонной книги открыт***')
            print()
        elif choice == '2':
            contacts = read_contacts()
            write_contacts(contacts)
            print('***Файл телефонной книги сохранен***')
            print()
        elif choice == '3':
            show_all_contacts()
        elif choice == '4':
            find_contact()
        elif choice == '5':
            add_contact()
            print('***Контакт добавлен***')
            print()
        elif choice == '6':
            update_contact()
            print()
        elif choice == '7':
            delete_contact()
            print()
        elif choice == '8':
            break
        else:
            print('Неверный ввод')

# Проверка условия главного скрипта
if __name__ == '__main__':
    main()