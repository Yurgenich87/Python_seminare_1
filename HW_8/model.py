import json
import json


class PhoneBook:
    def __init__(self):
        self.contacts_file = "contacts.txt"
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        with open(self.contacts_file, mode='r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                first_name, last_name, phone_number = line.strip().split(',')
                contact = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone_number': phone_number
                }
                self.contacts.append(contact)

    def save_contacts(self):
        with open(self.contacts_file, "w", encoding='utf-8') as file:
            file.truncate(0)  # очищаем файл
            for contact in self.contacts:
                file.write(f"{contact['first_name']},{contact['last_name']},{contact['phone_number']}\n")
    # def save_contacts(self):
    #     with open(self.contacts_file, "w", encoding='utf-8') as file:
    #         for contact in self.contacts:
    #             file.write(f"{contact['first_name']},{contact['last_name']},{contact['phone_number']}\n")

    def add_contact(self, first_name, last_name, phone_number):
        contact = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number
        }
        self.contacts.append(contact)
        self.save_contacts()
        print('-------Контакт добавлен-------')

    def search_contact(self, query):
        result = []
        for contact in self.contacts:
            if query in contact["first_name"] or \
                    query in contact["last_name"] or \
                    query in contact["phone_number"]:
                result.append(contact)
        return result

    def get_all_contacts(self):
        return self.contacts

    def remove_contact(self, contact_info):
        temp_contacts = []
        for contact in self.contacts:
            if (contact["first_name"] == contact_info["first_name"]
                    and contact["last_name"] == contact_info["last_name"]
                    and contact["phone_number"] == contact_info["phone_number"]):
                continue
            temp_contacts.append(contact)
        self.contacts = temp_contacts
        print('-------Кантакт удален-------')
        self.save_contacts()
        with open(self.contacts_file, "r", encoding="utf-8") as f:
            print(f.read())

    def update_contact(self, query, first_name, last_name, phone_number):
        for i, contact in enumerate(self.contacts):
            if query in contact["first_name"] or query in contact["last_name"] or query in contact["phone_number"]:
                updated_contact = {"first_name": first_name, "last_name": last_name, "phone_number": phone_number}
                self.contacts[i] = updated_contact
                self.save_contacts()
                return True
        return False
    def find_edit_contact(self):
        first_name, last_name, phone_number = self.view.get_contact_info()
        query = self.view.get_query(
            "Введите имя, фамилию или номер телефона контакта, которого нужно изменить: ")
        updated = self.phonebook.update_contact(query, first_name, last_name, phone_number)
        if updated:
            print('-------Кантакт изменен-------')
            self.phonebook.save_contacts()
        else:
            print('-------Контакт не найден-------')




