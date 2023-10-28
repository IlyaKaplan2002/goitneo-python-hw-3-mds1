from cli_bot_classes import (
    AddressBook,
    Record,
    InvalidNameError,
    InvalidPhoneError,
    InvalidBirthdayError,
    PhoneNotFoundError,
    RecordNotFoundError,
)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            if data:
                print(data)
        except ValueError:
            print("Give me name and phone/birthday please.")
        except IndexError:
            print("Give me a name please")
        except InvalidNameError:
            print("Invalid name")
        except InvalidPhoneError:
            print("Invalid phone number")
        except InvalidBirthdayError:
            print("Invalid birthday date")
        except PhoneNotFoundError:
            print("Phone not found")
        except RecordNotFoundError:
            print("Contact not found")
        except Exception:
            print("Unknown error occurred")

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts: AddressBook):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return "Contact added."


@input_error
def change_contact(args, contacts: AddressBook):
    name, phone = args
    contact: Record = contacts.find(name)

    if not contact:
        return "Contact doesn't exist."

    [oldPhone, *_] = contact.get_phones_strings()
    contact.edit_phone(oldPhone, phone)
    return "Contact changed."


@input_error
def get_contact(args, contacts: AddressBook):
    name = args[0]
    contact: Record = contacts.find(name)

    if not contact:
        return "Contact doesn't exist."

    [phone, *_] = contact.get_phones_strings()
    return f"{name}: {phone}"


@input_error
def get_all_contacts(contacts: AddressBook):
    for item in contacts.get_all_strings():
        print(item)

    return "Contacts showed."


@input_error
def add_birthday(args, contacts: AddressBook):
    name, birthday = args
    contact: Record = contacts.find(name)

    if not contact:
        return "Contact doesn't exist."

    contact.add_birthday(birthday)

    return "Birthday added"


@input_error
def get_birthday(args, contacts: AddressBook):
    name = args[0]
    contact: Record = contacts.find(name)

    if not contact:
        return "Contact doesn't exist."

    print(f"{name}: {contact.get_birthday()}")


@input_error
def get_birthdays_per_week(contacts: AddressBook):
    contacts.get_birthdays_per_week()


def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command = ""
        args = []
        try:
            command, *args = parse_input(user_input)
        except:
            pass

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, contacts)
        elif command == "change":
            change_contact(args, contacts)
        elif command == "phone":
            get_contact(args, contacts)
        elif command == "all":
            get_all_contacts(contacts)
        elif command == "add-birthday":
            add_birthday(args, contacts)
        elif command == "show-birthday":
            get_birthday(args, contacts)
        elif command == "birthdays":
            get_birthdays_per_week(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
