from collections import UserDict
from datetime import datetime
from get_birthdays_per_week import (
    get_birthdays_per_week as get_birthdays_per_week_helper,
)


class InvalidNameError(Exception):
    pass


class InvalidPhoneError(Exception):
    pass


class InvalidBirthdayError(Exception):
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
        if not self.is_valid(value):
            raise InvalidNameError
        super().__init__(value)

    def is_valid(self, value):
        return bool(value)


class Phone(Field):
    def __init__(self, value):
        if not self.is_valid(value):
            raise InvalidPhoneError
        super().__init__(value)

    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()


class Birthday(Field):
    def __init__(self, value):
        validated_date = self.is_valid(value)

        if not validated_date:
            raise InvalidBirthdayError

        super().__init__(validated_date)

    def is_valid(self, value):
        try:
            [day, month, year] = value.split(".")
            return datetime(year=int(year), month=int(month), day=int(day))
        except:
            return None


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def get_phones_strings(self):
        phones = []

        for item in self.phones:
            phones.append(str(item))

        return phones

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phones = self.get_phones_strings()

        if not phone in phones:
            raise PhoneNotFoundError

        index = phones.index(phone)
        self.phones.pop(index)

    def edit_phone(self, phone, new_phone):
        phones = self.get_phones_strings()

        if not phone in phones:
            raise PhoneNotFoundError

        index = phones.index(phone)
        self.phones[index] = Phone(new_phone)

    def find_phone(self, phone):
        phones = self.get_phones_strings()

        if not phone in phones:
            raise PhoneNotFoundError

        index = phones.index(phone)
        return self.phones[index]

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_birthday(self):
        return self.birthday

    def get_name(self):
        return self.name

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

    def get_all_strings(self):
        result = []

        for _, item in self.data.items():
            result.append(item.__str__())

        return result

    def get_birthdays_per_week(self):
        users = []

        for _, item in self.data.items():
            users.append(
                {"name": item.get_name().value, "birthday": item.get_birthday().value}
            )

        get_birthdays_per_week_helper(users)
