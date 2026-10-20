products = [
    {"id": 1, "name": "Мышь Logitech", "category": "Мыши", "price": 1500, "quantity": 10},
    {"id": 2, "name": "Мышь A4Tech", "category": "Мыши", "price": 900, "quantity": 4},
    {"id": 3, "name": "Клавиатура механическая", "category": "Клавиатуры", "price": 4500, "quantity": 6},
    {"id": 4, "name": "Клавиатура офисная", "category": "Клавиатуры", "price": 1200, "quantity": 0},
    {"id": 5, "name": "Монитор Samsung", "category": "Мониторы", "price": 18000, "quantity": 3},
    {"id": 6, "name": "Наушники JBL", "category": "Наушники", "price": 3500, "quantity": 8},
    {"id": 7, "name": "Веб-камера", "category": "Аксессуары", "price": 2800, "quantity": 2},
    {"id": 8, "name": "Микрофон USB", "category": "Аксессуары", "price": 4200, "quantity": 5},
    {"id": 9, "name": "Колонки", "category": "Акустика", "price": 2600, "quantity": 7},
    {"id": 10, "name": "USB-флешка 64 ГБ", "category": "Накопители", "price": 700, "quantity": 15}
]


def find_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def print_product(product):
    print(
        f'ID: {product["id"]} | {product["name"]} | '
        f'Категория: {product["category"]} | Цена: {product["price"]} руб. | '
        f'На складе: {product["quantity"]} шт.'
    )


def read_positive_int(prompt):
    try:
        number = int(input(prompt))
        if number <= 0:
            print("Ошибка: введите целое число больше нуля.")
            return None
        return number
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
        return None
