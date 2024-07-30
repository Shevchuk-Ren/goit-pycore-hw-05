
# TASK 4 with error handling

<code object input_error at 0x7eb768ca8ce0, file "/tmp/ipykernel_12/1641583946.py", line 2>

<code object inner at 0x7eb768c54e00, file "/tmp/ipykernel_12/1641583946.py", line 3>

<code object inner at 0x7eb768c54e00, file "/tmp/ipykernel_12/1641583946.py", line 3>

<code object inner at 0x7eb768c54e00, file "/tmp/ipykernel_12/1641583946.py", line 3>

<code object inner at 0x7eb768c54e00, file "/tmp/ipykernel_12/1641583946.py", line 3>


# TASK 4

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
      if len(args) < 2:
          return "Error: Not enough arguments."
      name, phone = args

      if name in contacts:
        contacts[name] = phone
        return 'Contact updated'
      else:
        return f'Error: Name {name} is not defined. Try again with correct name'


def show_phone(args, contacts):
    if len(args) < 1:
        return "Error: Not enough arguments. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"Error: Contact {name} not found."
    
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
   




def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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

