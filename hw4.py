import colorama

#  TASK 4

def input_error(func):
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"{colorama.Fore.RED}Error: Contact not found."
        except ValueError:
            return f"{colorama.Fore.RED}Error: Please provide a valid name and phone number."
        except IndexError:
            return f"{colorama.Fore.RED}Error: Not enough arguments provided."
        except Exception as e:
            return f"{colorama.Fore.RED}An unexpected error occurred: {e}"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    print(cmd)

    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError(f"{colorama.Fore.RED}Not enough arguments provided.")
    name, phone = args
    contacts[name] = phone

    return f"{colorama.Fore.LIGHTBLUE_EX}Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError(f"{colorama.Fore.RED}Not enough arguments provided.")
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"{colorama.Fore.LIGHTBLUE_EX}Contact updated."
    else:
        raise KeyError(f"{colorama.Fore.RED}Name {name} not found.")

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError(f"{colorama.Fore.RED}No name provided.")
    name = args[0]
    if name in contacts:
        return f"{colorama.Fore.LIGHTBLUE_EX}{name}'s phone number is {contacts[name]}"
    else:
        raise KeyError(f"{colorama.Fore.RED}Contact {name} not found.")
    
@input_error
def show_all(contacts):
    if not contacts:
        return f"{colorama.Fore.RED}No contacts found."
    result = f"{colorama.Fore.LIGHTBLUE_EX}All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.strip()

def main():
    contacts = {}
    print(f"{colorama.Fore.LIGHTBLUE_EX}Welcome to the assistant bot!")
    while True:
        user_input = input(f"{colorama.Fore.LIGHTBLUE_EX}Enter {colorama.Fore.LIGHTMAGENTA_EX}a command:  {colorama.Fore.LIGHTBLUE_EX}")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(f"{colorama.Fore.LIGHTBLUE_EX}How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(f"{colorama.Fore.LIGHTBLUE_EX}Invalid command.")

if __name__ == "__main__":
    main()
