class Contact:
    def __init__(self, name, surname, phone_number, favorite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite
        self.additional_information = kwargs

    def __str__(self):
        res = [
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}',
            f'Телефон: {self.phone_number}',
            f'В избранных: {"да" if self.favorite else "нет"}'
        ]
        if self.additional_information:
            res.append('Дополнительная информация:')
            for key, value in self.additional_information.items():
                res.append(f'\t{key}: {value}')
        return '\n'.join(res)

    def __repr__(self):
        return self.__str__()


class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contats = []

    def display(self):
        print('*' * 50)
        print('Спосок всех контактов:')
        for contact in self.contats:
            print(contact)
        print('*' * 50)

    def add(self, *args, **kwargs):
        print('*' * 50)
        self.contats.append(Contact(*args, **kwargs))
        print('Контакт добавлен.')
        print('*' * 50)

    def del_by_phone(self, phone_number):
        print('*' * 50)
        for contact in self.contats:
            if contact.phone_number == phone_number:
                self.contats.remove(contact)
                print(f'Удален контакс с номером {phone_number}')
                print('*' * 50)
                return
        print(f'Контака с номером {phone_number} не существует.')
        print('*' * 50)

    def get_all_fav(self):
        print('*' * 50)
        print('Список любимых контактов')
        for contact in (contact for contact in self.contats if contact.favorite):
            print(contact)
        print('*' * 50)

    def finnd_by_name(self, name, surname):
        print('*' * 50)
        print(f'Найденые контакты с именем и фамилий {name} {surname}')
        for contats in (contact for contact in self.contats if contact.name == name and contact.surname == surname):
            print(contats)
        print('*' * 50)


if __name__ == "__main__":
    pb = PhoneBook('pb')
    pb.add('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    pb.add('Marry', 'Smith', '+71234067809', telegram='@marry', email='marry@smith.com', favorite=True)
    pb.add('Marry', 'Smith', '+71234037809', telegram='@marry', email='marry@smith.com')
    pb.add('Marry', 'Smith', '+71238037809', telegram='@marry2', email='marry2@smith.com')
    pb.display()
    pb.del_by_phone('+71234037809')
    pb.get_all_fav()
    pb.finnd_by_name(*'Marry Smith'.split(' '))
