from task1_show_products import show_products
from task2_search import find_product
from task3_category import filter_category
from task4_stock import check_stock
from task5_restock import restock_product
from task6_sell import sell_product
from task7_statistics import show_statistics
from task8_sort import sort_products
from task10_cart import cart_menu


def main():
    while True:
        print(" УЧЁТ ТОВАРОВ МАГАЗИНА ")
        print("1. Показать все товары")
        print("2. Найти товар по названию")
        print("3. Показать товары выбранной категории")
        print("4. Проверить остатки на складе")
        print("5. Пополнить склад")
        print("6. Продать товар")
        print("7. Показать статистику")
        print("8. Отсортировать товары")
        print("9. Корзина покупателя")
        print("0. Завершить работу")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_products()
        elif choice == "2":
            find_product()
        elif choice == "3":
            filter_category()
        elif choice == "4":
            check_stock()
        elif choice == "5":
            restock_product()
        elif choice == "6":
            sell_product()
        elif choice == "7":
            show_statistics()
        elif choice == "8":
            sort_products()
        elif choice == "9":
            cart_menu()
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Ошибка: такого пункта меню нет. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
