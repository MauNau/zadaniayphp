from data import find_by_id, print_product, read_positive_int


def restock_product():
    product_id = read_positive_int("Введите ID товара: ")
    if product_id is None:
        return

    product = find_by_id(product_id)
    if product is None:
        print("Товар с таким ID не найден.")
        return

    amount = read_positive_int("Сколько единиц добавить: ")
    if amount is None:
        return

    product["quantity"] += amount
    print("Склад пополнен. Обновлённая информация:")
    print_product(product)


if __name__ == "__main__":
    restock_product()
