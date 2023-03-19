class PhoneBookView:
    def __init__(self):
        pass

    def get_menu_choice(self):
        print('------------------------')
        print("  Выберите действие:")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Найти контакт")
        print("4. Вывести все контакты")
        print("5. Изменить контакт")
        print("0. Выйти")
        choice = input()
        return choice

    def get_contact_info(self):
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        phone_number = input("Введите номер телефона: ")
        return first_name, last_name, phone_number

    def get_search_term(self):
        search_term = input("Введите имя, фамилию или номер телефона: ")
        print('------------------------')
        return search_term

    def display_results(self, results):
        if results:
            for contact in results:
                print(f"{contact['first_name']} {contact['last_name']}: {contact['phone_number']}")
        else:
            print("Контакт не найден")

    def display_all_contacts(self, contacts):
        if contacts:
            for contact in contacts:
                print(f"{contact['first_name']} {contact['last_name']}: {contact['phone_number']}")
        else:
            print("Контакты отсутствуют")

    def get_query(self, message):
        print(message)
        query = input()
        return query
