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
    if not phone_book.get(user[0]):
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


def show_all():
    for key, value in phone_book.items():
        print(key, value)


def final():
    print('Good bye!')
    return exit()


def greeting():
    print("How can I help you?")


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


def get_handler2(y):
    return command_dict2[y]


def main():
    while True:
        command = input().lower().strip()

        if command in command_dict1:
            foo = get_handler1(command)
            foo()
        else:
            command = command.split(" ")
            contact = command[1:]

            if command[0] in command_dict2:
                func = get_handler2(command[0])
                func(contact)
            else:
                print("This is an incorrect command. Try again, please")


if __name__ == "__main__":
    main()
