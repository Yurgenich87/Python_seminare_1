from HW_8.model import PhoneBook
from HW_8.view import PhoneBookView


class PhoneBookController:
    def __init__(self):
        self.view = PhoneBookView()
        self.phonebook = PhoneBook()

    def run(self):
        choice = ""
        while choice != "0":
            choice = self.view.get_menu_choice()
            if choice == "1":
                first_name, last_name, phone_number = self.view.get_contact_info()
                self.phonebook.add_contact(first_name, last_name, phone_number)
            elif choice == "2":
                first_name, last_name, phone_number = self.view.get_contact_info()
                self.phonebook.remove_contact({"first_name": first_name, "last_name": last_name, "phone_number": phone_number})

            elif choice == "3":
                search_term = self.view.get_search_term()
                results = self.phonebook.search_contact(search_term)
                self.view.display_results(results)
            elif choice == "4":
                contacts = self.phonebook.get_all_contacts()
                self.view.display_all_contacts(contacts)
            elif choice == "5":
                first_name, last_name, phone_number = self.view.get_contact_info()
                query = self.view.get_query(
                    "Введите имя, фамилию или номер телефона контакта, которого нужно изменить: ")
                updated = self.phonebook.update_contact(query, first_name, last_name, phone_number)
                if updated:
                    print('-------Кантакт изменен-------')
                    self.phonebook.save_contacts()
                else:
                    print('-------Контакт не найден-------')

            elif choice == "0":
                print("До свидания")
            else:
                print("Неверный выбор")
