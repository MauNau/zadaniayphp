from data import products, print_product


def sort_products():
    print("1. Цена: от меньшей к большей")
    print("2. Цена: от большей к меньшей")
    print("3. Название: по алфавиту")
    print("4. Количество: от меньшего к большему")
    choice = input("Выберите способ сортировки: ").strip()

    if choice == "1":
        sorted_items = sorted(products, key=lambda item: item["price"])
    elif choice == "2":
        sorted_items = sorted(products, key=lambda item: item["price"], reverse=True)
    elif choice == "3":
        sorted_items = sorted(products, key=lambda item: item["name"].lower())
    elif choice == "4":
        sorted_items = sorted(products, key=lambda item: item["quantity"])
    else:
        print("Неизвестный вариант сортировки.")
        return

    print("Отсортированный ассортимент")
    for product in sorted_items:
        print_product(product)


if __name__ == "__main__":
    sort_products()
