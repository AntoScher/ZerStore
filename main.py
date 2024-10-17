# main.py

from store import Store

# Создание экземпляра класса Store
store = Store("Fresh Market", "123 Main St")

# Добавление товаров
store.add_item("apples", 0.5)
store.add_item("bananas", 0.75)

# Получение цены товара
print(store.get_price("apples"))  # Вывод: 0.5
print(store.get_price("oranges"))  # Вывод: None (товар отсутствует)

# Обновление цены товара
store.update_price("apples", 0.6)
print(store.get_price("apples"))  # Вывод: 0.6

# Удаление товара
store.remove_item("bananas")
print(store.get_price("bananas"))  # Вывод: None (товар удален)
