from data import products, print_product


def find_product():
    query = input("Введите название товара или его часть: ").strip().lower()
    found = []
    for product in products:
        if query in product["name"].lower():
            found.append(product)

    if found:
        for product in found:
            print_product(product)
    else:
        print("Подходящие товары не найдены.")


if __name__ == "__main__":
    find_product()
