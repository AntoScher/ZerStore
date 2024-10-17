from store import Store

def main():
    name = input("Введите название магазина: ")
    address = input("Введите адрес магазина: ")

    store = Store(name, address)

    while True:
        item_name = input("Введите название товара: ")
        while True:
            try:
                price = float(input("Введите цену товара: "))
                break
            except ValueError:
                print("Неверный ввод цены. Пожалуйста, введите число.")

        store.add_item(item_name, price)

        continue_input = input("Будете ли вы еще вводить атрибуты? (Y/N): ")
        if continue_input.lower() != 'y':
            break

    def display_items():
        print(f"Название магазина: {store.name}")
        print(f"Адрес магазина: {store.address}")
        print("Товары:")
        for i, (item, price) in enumerate(store.items.items(), 1):
            print(f"{i}. {item}: {price}")

    def save_to_file():
        with open('goods.txt', 'w') as file:
            file.write(f"Название магазина: {store.name}\n")
            file.write(f"Адрес магазина: {store.address}\n")
            file.write("Товары:\n")
            for item, price in store.items.items():
                file.write(f"{item}: {price}\n")

    display_items()
    save_to_file()

    while True:
        edit_choice = input("Будете ли вы что-то редактировать в файле goods.txt? (Y/N): ")
        if edit_choice.lower() == 'y':
            print("Выберите действие:\n1. Отредактировать пару item_name, price\n2. Добавить пару item_name, price\n3. Удалить пару item_name, price")
            action = input("Введите номер действия: ")
            if action == '1':
                while True:
                    try:
                        index = int(input("Введите номер пары для редактирования: ")) - 1
                        if 0 <= index < len(store.items):
                            new_item, new_price = input("Введите новое название товара и цену через '-': ").split('-')
                            new_price = float(new_price)
                            key_to_update = list(store.items.keys())[index]
                            store.items.pop(key_to_update)
                            store.add_item(new_item, new_price)
                            save_to_file()
                            print("Пара отредактирована.")
                            break
                        else:
                            print("Неверный номер.")
                    except ValueError:
                        print("Неверный ввод. Пожалуйста, попробуйте снова.")
            elif action == '2':
                while True:
                    try:
                        new_item, new_price = input("Введите новое название товара и цену через '-': ").split('-')
                        new_price = float(new_price)
                        store.add_item(new_item, new_price)
                        save_to_file()
                        print("Пара добавлена.")
                        break
                    except ValueError:
                        print("Неверный ввод. Пожалуйста, попробуйте снова.")
            elif action == '3':
                while True:
                    try:
                        index = int(input("Введите номер пары для удаления: ")) - 1
                        if 0 <= index < len(store.items):
                            key_to_remove = list(store.items.keys())[index]
                            store.remove_item(key_to_remove)
                            save_to_file()
                            print("Пара удалена.")
                            break
                        else:
                            print("Неверный номер.")
                    except ValueError:
                        print("Неверный ввод. Пожалуйста, попробуйте снова.")
            else:
                print("Неверное действие.")
            display_items()
        elif edit_choice.lower() == 'n':
            display_items()
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()

