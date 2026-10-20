from data import products


def show_statistics():
    if not products:
        print("Ассортимент пуст.")
        return

    total_units = 0
    stock_value = 0
    sum_prices = 0
    category_units = {}

    for product in products:
        total_units += product["quantity"]
        stock_value += product["price"] * product["quantity"]
        sum_prices += product["price"]

        category = product["category"]
        if category not in category_units:
            category_units[category] = 0
        category_units[category] += product["quantity"]

    expensive = max(products, key=lambda item: item["price"])
    cheapest = min(products, key=lambda item: item["price"])
    largest_category = max(category_units, key=category_units.get)
    average_price = sum_prices / len(products)

    print("--- Статистика магазина ---")
    print(f"Различных позиций: {len(products)}")
    print(f"Всего единиц на складе: {total_units}")
    print(f"Общая стоимость товаров на складе: {stock_value} руб.")
    print(f'Самый дорогой товар: {expensive["name"]} — {expensive["price"]} руб.')
    print(f'Самый дешёвый товар: {cheapest["name"]} — {cheapest["price"]} руб.')
    print(f"Больше всего единиц в категории: {largest_category} ({category_units[largest_category]} шт.)")
    print(f"Средняя цена одной позиции: {average_price:.2f} руб.")


if __name__ == "__main__":
    show_statistics()
