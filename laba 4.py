def format_price(price):
    return f"ціна: {price:.2f} грн"


def check_availability(*items):
    store = {
        "хліб": True,
        "молоко": True,
        "масло": False,
        "цукор": True,
        "сир": False,
        "яблуко": True}

    result = {}
    for item in items:
        result[item] = store.get(item, False)
    return result

def process_order():
    print("Доступні товари: хліб, молоко, масло, цукор, сир, яблуко")
    order = input("Введіть товари через кому: ").lower().split(",")
    order = [item.strip() for item in order]

    available = check_availability(*order)

    if all(available.values()):
        print("Усі товари є в наявності ✅")
        prices = {"хліб": 25.5, "молоко": 32.0, "масло": 90.0, "цукор": 28.7, "сир": 70.0, "яблуко": 15.5}
        total = sum(prices[item] for item in order)

        action = input("Оберіть дію: 'купити' або 'переглянути ціну': ").lower()
        if action == "переглянути ціну":
            print(format_price(total))
        elif action == "купити":
            print(f"Ви успішно купили товари на суму {format_price(total)} 🎉")
        else:
            print("Невідома дія.")
    else:
        print("Не всі товари є в наявності ❌")
        for item, status in available.items():
            print(f"{item}: {'є' if status else 'немає'}")

def main():
    process_order()


if __name__ == '__main__':
    main()