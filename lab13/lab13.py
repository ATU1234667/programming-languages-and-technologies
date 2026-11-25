def main():
    products = []
    menu = (
        "1 — добавить товар\n"
        "2 — удалить товар\n"
        "3 — показать список\n"
        "4 — найти товар\n"
        "0 — выйти"
    )
    print("Список покупок")
    print(menu)

    while True:
        action = input("\nКоманда: ").strip()
        if action == "0":
            print("Программа завершена.")
            break

        if action == "1":
            name = input("Название: ").strip()
            if not name:
                print("Название не может быть пустым.")
            else:
                products.append(name)
                print(f"Добавлено: {name}")

        elif action == "2":
            name = input("Название для удаления: ").strip()
            if not name:
                print("Название не может быть пустым.")
            elif name in products:
                products.remove(name)
                print(f"Удалено: {name}")
            else:
                print("Такого товара нет.")

        elif action == "3":
            if not products:
                print("Список пуст.")
            else:
                print("Покупки:")
                for number, name in enumerate(products, start=1):
                    print(f"{number}. {name}")

        elif action == "4":
            query = input("Введите часть названия: ").strip().casefold()
            if not query:
                print("Запрос не может быть пустым.")
            else:
                matches = [name for name in products if query in name.casefold()]
                if matches:
                    print("Найдено: " + ", ".join(matches))
                else:
                    print("Совпадений нет.")

        else:
            print("Неизвестная команда. Выберите 0, 1, 2, 3 или 4.")


if __name__ == "__main__":
    main()
