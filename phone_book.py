import random

class Data:
    def __init__(my, name, phone_number, address):
        my.name = name
        my.phone_number = phone_number
        my.address = address
        my.left = None
        my.right = None

    def __str__(my):
        information = ""
        information += f"Name: {my.name}\n"
        information += f"phone Number: {my.phone_number}\n"
        information += f"Address: {my.address}\n"
        return information


class Info():
    def __init__(my):
        my.info = None


    def guidelines(my, name, phone_number, address):
        my.info = Data(name, phone_number, address)


    def add_input(my, name, phone_number, address):
        if my.info:
            my.enter_data(my.info, name, phone_number, address)
        else:
            my.guidelines(name, phone_number, address)


    def enter_data(my, lastest_data, name, phone_number, address):
        if name > lastest_data.name:
            if lastest_data.right:
                my.enter_data(lastest_data.right, name, phone_number, address)
            else:
                lastest_data.right = Data(name, phone_number, address)
        else:
            if lastest_data.left:
                my.enter_data(lastest_data.left, name, phone_number, address)
            else:
                lastest_data.left = Data(name, phone_number, address)


    def locate(my, name, lastest_data = None):
        if not lastest_data:
            lastest_data = my.info

        if lastest_data.name == name:
            return lastest_data
        elif name > lastest_data.name:
            if lastest_data.right:
                return my.locate(name, lastest_data.right)
            else:
                return None
        else:
            if lastest_data.left:
                return my.locate(name, lastest_data.left)
            else:
                return None


    def erase(my, name):
        if not my.info:
            return False
        elif my.info.name == name:
            if not my.info.left and not my.info.right:
                my.info = None
            elif my.info.left and not my.info.right:
                my.info = my.info.left
            elif my.info.right and not my.info.left:
                my.info = my.info.right
            else:
                erase_main = my.info
                erase_data = my.info.right
                while erase_data.left:
                    erase_main = erase_data
                    erase_data = erase_data.left

                my.info.name = erase_data.name
                my.info.phone_number = erase_data.phone_number
                my.info.address = erase_data.address

                if erase_data.right:
                    if erase_main.name > erase_data.name:
                        erase_main.left = erase_data.right
                    else:
                        erase_main.right = erase_data.right
                else:
                    if erase_data.name < erase_main.name:
                        erase_main.left = None
                    else:
                        erase_main.right = None
            return True

        main = None
        data = my.info

        while data and data.name != name:
            main = data
            if name < data.name:
                data = data.left
            elif name > data.name:
                data = data.right

        if not data or data.name != name:
            return False

        elif not data.left and not data.right:
            if name < main.name:
                main.left = None
            else:
                main.right = None
            return True

        elif data.left and not data.right:
            if name < main.name:
                main.left = data.left
            else:
                main.right = data.left
            return True

        elif not data.left and data.right:
            if name < main.name:
                main.left = data.right
            else:
                main.right = data.right
            return True

        else:
            erase_main = data
            erase_data = data.right
            while erase_data.left:
                erase_main = erase_data
                erase_data = erase_data.left

            data.name = erase_data.name
            data.phone_number = erase_data.phone_number
            data.address = erase_data.address

            if erase_data.right:
                if erase_main.name > erase_data.name:
                    erase_main.left = erase_data.right
                elif erase_main.name < erase_data.name:
                    erase_main.right = erase_data.right
            else:
                if erase_data.name < erase_main.name:
                    erase_main.left = None
                else:
                    erase_main.right = None

            return True


    def traverse(my, lastest_data):
        if lastest_data:
            my.traverse(lastest_data.left)
            print (lastest_data)
            my.traverse(lastest_data.right)


class Bin_tree:
    def __init__(my):
        my.info = None


    def guidelines(my, name, phone_number, address):
        my.info = Data(name, phone_number, address)


    def add_input(my, name, phone_number, address):
        if my.info:
            my.enter_data(my.info, name, phone_number, address)
        else:
            my.guidelines(name, phone_number, address)


    def enter_data(my, lastest_data, name, phone_number, address):
        if phone_number > lastest_data.phone_number:
            if lastest_data.right:
                my.enter_data(lastest_data.right, name, phone_number, address)
            else:
                lastest_data.right = Data(name, phone_number, address)
        else:
            if lastest_data.left:
                my.enter_data(lastest_data.left, name, phone_number, address)
            else:
                lastest_data.left = Data(name, phone_number, address)


    def locate(my, phone_number, lastest_data=None):
        if not lastest_data:
            lastest_data = my.info

        if lastest_data.phone_number == phone_number:
            return lastest_data
        elif phone_number > lastest_data.phone_number:
            if lastest_data.right:
                return my.locate(phone_number, lastest_data.right)
            else:
                return None
        else:
            if lastest_data.left:
                return my.locate(phone_number, lastest_data.left)
            else:
                return None


    def erase(my, phone_number):
        if not my.info:
            return False
        elif my.info.phone_number == phone_number:
            if not my.info.left and not my.info.right:
                my.info = None
            elif my.info.left and not my.info.right:
                my.info = my.info.left
            elif my.info.right and not my.info.left:
                my.info = my.info.right
            else:
                erase_main = my.info
                erase_data = my.info.right
                while erase_data.left:
                    erase_main = erase_data
                    erase_data = erase_data.left

                my.info.name = erase_data.name
                my.info.phone_number = erase_data.phone_number
                my.info.address = erase_data.address

                if erase_data.right:
                    if erase_main.phone_number > erase_data.phone_number:
                        erase_main.left = erase_data.right
                    else:
                        erase_main.right = erase_data.right
                else:
                    if erase_data.phone_number < erase_main.phone_number:
                        erase_main.left = None
                    else:
                        erase_main.right = None
            return True

        main = None
        data = my.info

        while data and data.phone_number != phone_number:
            main = data
            if phone_number < data.phone_number:
                data = data.left
            elif phone_number > data.phone_number:
                data = data.right

        if not data or data.phone_number != phone_number:
            return False

        elif not data.left and not data.right:
            if phone_number < main.phone_number:
                main.left = None
            else:
                main.right = None
            return True

        elif data.left and not data.right:
            if phone_number < main.phone_number:
                main.left = data.left
            else:
                main.right = data.left
            return True

        elif not data.left and data.right:
            if phone_number < main.phone_number:
                main.left = data.right
            else:
                main.right = data.right
            return True

        else:
            erase_main = data
            erase_data = data.right
            while erase_data.left:
                erase_main = erase_data
                erase_data = erase_data.left

            data.name = erase_data.name
            data.phone_number = erase_data.phone_number
            data.address = erase_data.address

            if erase_data.right:
                if erase_main.phone_number > erase_data.phone_number:
                    erase_main.left = erase_data.right
                elif erase_main.phone_number < erase_data.phone_number:
                    erase_main.right = erase_data.right
            else:
                if erase_data.phone_number < erase_main.phone_number:
                    erase_main.left = None
                else:
                    erase_main.right = None

            return True

def main():
    names = ["Tom", "Jerry"]
    phones = ["123", "0884624315"]
    addresses = ["House 4", "House 5"]
    phone_tree = Bin_tree()
    details = Info()

    for i in range(len(names)):
        details.add_input(names[i], phones[i], addresses[i])
        phone_tree.add_input(names[i], phones[i], addresses[i])

    print(details.locate("Zach"))

    details.erase("Cliodhna")
    phone_tree.erase("0855881892")

if __name__ == "__main__":
    main()