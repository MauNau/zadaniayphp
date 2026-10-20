from data import products, print_product


def show_products():
    total_cost = 0
    print("Ассортимент товаров")
    for product in products:
        print_product(product)
        total_cost += product["price"] * product["quantity"]
    print(f"Общая стоимость всех товаров на складе: {total_cost} руб.")


if __name__ == "__main__":
    show_products()
