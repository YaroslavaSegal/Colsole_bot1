phone_book = dict()


def input_error(func):
    def inner(x):
        try:
            result = func(x)
            return result
        except IndexError as Error:
            return Error
        except KeyError as Error:
            return Error
        except ValueError as Error:
            return Error
        except TypeError as Error:
            return Error
    return inner


@input_error
def add_contact(user):
    if not user:
        raise ValueError("Give me user name and phone please")
    if phone_book.get(user[0]):
        raise KeyError("Contact already exists")
    else:
        phone_book[user[0]] = user[1]
        return f'contact {user[0]} has been added with phone {user[1]}'


@input_error
def change_contact(user):
    if not user:
        raise ValueError("Give me user name and phone please")
    if phone_book.get(user[0]):
        phone_book[user[0]] = user[1]
        return f'contact {user[0]} has been changed to phone {user[1]}'
    else:
        raise IndexError("No such name in phone book")


@input_error
def print_phone(x):
    if not x:
        raise TypeError("Enter name please")
    name = ''.join(x)
    phone = phone_book[name]
    return f'phone of user {name} is {phone}'


def show_all():
    return phone_book


def final():
    return 'Good bye!'


def greeting():
    return "How can I help you?"


command_dict1 = {
    "good bye": final,
    "close": final,
    "exit": final,
    "hello": greeting,
    "show all": show_all
}

command_dict2 = {
    "add": add_contact,
    "change": change_contact,
    "phone": print_phone
}


def get_handler1(x):
    return command_dict1[x]


def get_handler2(x):
    return command_dict2[x]


def main():
    while True:
        command = input().lower().strip()

        if command in command_dict1:
            result = get_handler1(command)()
            print(result)
            if result == "Good bye!":
                break
        else:
            command = command.split(" ")
            contact = command[1:]

            if command[0] in command_dict2:
                result = get_handler2(command[0])(contact)
                if result is not None:
                    print(result)
            else:
                print("This is an incorrect command. Try again, please")


if __name__ == "__main__":
    main()
