from collections import UserDict


class InvalidNameError(Exception):
    pass


class InvalidPhoneError(Exception):
    pass


class PhoneNotFoundError(Exception):
    pass


class RecordNotFoundError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.is_valid():
            raise InvalidNameError

    def is_valid(self):
        return bool(self.value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.is_valid():
            raise InvalidPhoneError

    def is_valid(self):
        try:
            int(self.value)
        except:
            return False

        return len(self.value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __get_phones_strings(self):
        phones = []

        for item in self.phones:
            phones.append(str(item))

        return phones

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phones = self.__get_phones_strings()

        if not phone in phones:
            raise PhoneNotFoundError

        index = phones.index(phone)
        self.phones.pop(index)

    def edit_phone(self, phone, new_phone):
        phones = self.__get_phones_strings()

        if not phone in phones:
            raise PhoneNotFoundError

        index = phones.index(phone)
        self.phones[index] = Phone(new_phone)

    def find_phone(self, phone):
        phones = self.__get_phones_strings()

        if not phone in phones:
            raise PhoneNotFoundError

        index = phones.index(phone)
        return self.phones[index]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record

    def find(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise RecordNotFoundError

    def delete(self, name):
        try:
            del self.data[name]
        except KeyError:
            raise RecordNotFoundError
