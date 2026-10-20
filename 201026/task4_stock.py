from data import products


def check_stock():
    no_stock = []
    less_than_five = []
    five_or_more = []

    for product in products:
        if product["quantity"] == 0:
            no_stock.append(product)
        elif product["quantity"] < 5:
            less_than_five.append(product)
        else:
            five_or_more.append(product)

    groups = [
        ("Товаров нет на складе", no_stock),
        ("Меньше 5 единиц", less_than_five),
        ("5 единиц или больше", five_or_more)
    ]

    for title, items in groups:
        print("\\n---", title, "---")
        if items:
            for product in items:
                print(f'{product["name"]} — {product["quantity"]} шт.')
        else:
            print("Таких товаров нет.")


if __name__ == "__main__":
    check_stock()
