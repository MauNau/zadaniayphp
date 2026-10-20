from data import find_by_id, read_positive_int


def sell_product():
    product_id = read_positive_int("Введите ID товара: ")
    if product_id is None:
        return

    product = find_by_id(product_id)
    if product is None:
        print("Товар с таким ID не найден.")
        return

    amount = read_positive_int("Сколько единиц продать: ")
    if amount is None:
        return

    if product["quantity"] < amount:
        print(f'Недостаточно товара. На складе: {product["quantity"]} шт.')
        return

    product["quantity"] -= amount
    total = product["price"] * amount
    print(f"Продажа выполнена. Итоговая стоимость: {total} руб.")
    print(f'Остаток товара «{product["name"]}»: {product["quantity"]} шт.')


if __name__ == "__main__":
    sell_product()
