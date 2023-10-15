def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        pass


def add_contact(args, contacts):
    name = ""
    phone = ""
    try:
        name, phone = args
    except:
        return "Invalid args."
    contacts[name] = phone
    return "Contact added."


def get_contact(args, contacts):
    name = ""
    try:
        name = args[0]
    except:
        return "Invalid args."
    if not contacts.get(name):
        return "Contact doesn't exist."
    return f"{name}: {contacts[name]}"


def change_contact(args, contacts):
    name = ""
    phone = ""
    try:
        name, phone = args
    except:
        return "Invalid args."
    if not contacts.get(name):
        return "Contact doesn't exist."
    contacts[name] = phone
    return "Contact changed."


def get_all_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

    return "Contacts showed."


def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            get_all_contacts(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
