from store import Store

def main():
    name = input("Введите название магазина: ")
    address = input("Введите адрес магазина: ")

    store = Store(name, address)

    while True:
        item_name = input("Введите название товара: ")
        price = float(input("Введите цену товара: "))

        store.add_item(item_name, price)

        continue_input = input("Будете ли вы еще вводить атрибуты? (Y/N): ")
        if continue_input.lower() != 'y':
            break

    # Вывод списка введенных атрибутов
    print(f"Название магазина: {store.name}")
    print(f"Адрес магазина: {store.address}")
    print("Товары:")
    for item, price in store.items.items():
        print(f"- {item}: {price}")

    # Сохранение в файл goods.txt
    with open('goods.txt', 'w') as file:
        file.write(f"Название магазина: {store.name}\n")
        file.write(f"Адрес магазина: {store.address}\n")
        file.write("Товары:\n")
        for item, price in store.items.items():
            file.write(f"- {item}: {price}\n")

if __name__ == "__main__":
    main()
