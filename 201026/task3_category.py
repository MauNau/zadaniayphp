from data import products, print_product


def filter_category():
    categories = set()
    for product in products:
        categories.add(product["category"])

    print("Уникальные категории:")
    for category in sorted(categories):
        print("-", category)

    query = input("Введите категорию: ").strip().lower()
    found = [product for product in products if product["category"].lower() == query]

    if found:
        for product in found:
            print_product(product)
    else:
        print("В этой категории товаров нет.")


if __name__ == "__main__":
    filter_category()
