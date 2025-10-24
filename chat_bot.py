def input_error(func):
    """Decorator that handles user input errors gracefully."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter correct user name."
        except IndexError:
            return "Enter user name."
    return inner


@input_error
def add_contact(args, contacts):
    """Add new contact: add <name> <phone>"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """Change existing contact: change <name> <new_phone>"""
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    """Show phone by name: phone <name>"""
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    """Show all saved contacts"""
    if not contacts:
        return "No contacts saved yet."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result


def parse_input(user_input):
    """Split input into command and arguments"""
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")
            

if __name__ == "__main__":
    main()
