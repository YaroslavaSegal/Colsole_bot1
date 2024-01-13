def console_bot():
    phone_book = dict()

    def input_error(func):
        def inner(x):
            try:
                result = func(x)
                return result
            except IndexError:
                print("Enter phone please")
            except KeyError:
                print("No such name in phone book")
            except ValueError:
                print("Give me user name and phone please")
            except TypeError:
                print("Enter name please")

        return inner

    @input_error
    def add_contact(user):
        if not user:
            raise ValueError
        phone_book[user[0]] = user[1]
        return phone_book

    @input_error
    def change_contact(user):
        if not user:
            raise ValueError
        if phone_book.get(user[0]):
            phone_book[user[0]] = user[1]
            return phone_book
        else:
            return phone_book[user[0]]

    @input_error
    def print_phone(x):
        if not x:
            raise TypeError
        name = ''.join(x)
        phone = phone_book[name]
        print(phone)

    while True:
        command = input().lower().strip()
        if command == ".":
            break
        elif command == 'goodbye' or command == "close" or command == 'exit':
            print('Good bye!')
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "show all":
            for key, value in phone_book.items():
                print(key, value)
        else:
            command = command.split(" ")
            contact = command[1:]

            if command[0] == "add":
                add_contact(contact)
            elif command[0] == 'change':
                change_contact(contact)
            elif command[0] == "phone":
                print_phone(contact)
            else:
                print("This is an incorrect command. Try again, please")


if __name__ == "__main__":
    console_bot()
