from data import products, find_by_id, read_positive_int


def show_cart(cart):
    if not cart:
        print("Корзина пуста.")
        return

    total = 0
    print("Корзина")
    for product_id, amount in cart.items():
        product = find_by_id(product_id)
        line_total = product["price"] * amount
        total += line_total
        print(f'{product["name"]}: {amount} шт. x {product["price"]} руб. = {line_total} руб.')
    print(f"Общая сумма: {total} руб.")


def add_to_cart(cart):
    product_id = read_positive_int("Введите ID товара: ")
    if product_id is None:
        return
    product = find_by_id(product_id)
    if product is None:
        print("Товар не найден.")
        return

    amount = read_positive_int("Введите количество: ")
    if amount is None:
        return

    already_added = cart.get(product_id, 0)
    if already_added + amount > product["quantity"]:
        print(f'На складе доступно {product["quantity"]} шт.; в корзине уже {already_added} шт.')
        return

    cart[product_id] = already_added + amount
    print("Товар добавлен в корзину.")


def remove_from_cart(cart):
    if not cart:
        print("Корзина пуста.")
        return
    show_cart(cart)
    product_id = read_positive_int("Введите ID товара для удаления: ")
    if product_id is None:
        return
    if product_id in cart:
        del cart[product_id]
        print("Товар удалён из корзины.")
    else:
        print("Такого товара в корзине нет.")


def checkout(cart):
    if not cart:
        print("Корзина пуста.")
        return

    for product_id, amount in cart.items():
        product = find_by_id(product_id)
        if product is None or product["quantity"] < amount:
            print("Не удалось оформить заказ: товара недостаточно или он не найден.")
            print("Остатки на складе не изменены.")
            return

    total = 0
    for product_id, amount in cart.items():
        product = find_by_id(product_id)
        total += product["price"] * amount
        product["quantity"] -= amount

    print(f"Заказ успешно оформлен. Итого: {total} руб.")
    cart.clear()


def cart_menu():
    cart = {}
    while True:
        print("Меню корзины")
        print("1. Показать корзину")
        print("2. Добавить товар")
        print("3. Удалить товар")
        print("4. Оформить заказ")
        print("5. Вернуться назад")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_cart(cart)
        elif choice == "2":
            add_to_cart(cart)
        elif choice == "3":
            remove_from_cart(cart)
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    cart_menu()
