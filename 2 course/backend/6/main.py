import datetime
from decimal import Decimal

goods = {
    "Вареники": [
        {"amount": Decimal("0.5"), "expiration_date": datetime.date(2023, 7, 15)},
        {"amount": Decimal("2"), "expiration_date": datetime.date(2023, 8, 1)},
    ],
    "Вода": [{"amount": Decimal("1.5"), "expiration_date": None}],
}


def add(product_name, amount, expiration_date=None):
    if product_name in goods:
        goods[product_name].append(
            {"amount": Decimal(amount), "expiration_date": expiration_date}
        )
    else:
        goods[product_name] = [
            {"amount": Decimal(amount), "expiration_date": expiration_date}
        ]


def add_by_note(note):
    parts = note.split(", ")
    product_name = parts[0]
    amount = Decimal(parts[1])
    expiration_date = (
        None
        if parts[2] == "None"
        else datetime.datetime.strptime(parts[2], "%Y-%m-%d").date()
    )
    add(product_name, amount, expiration_date)


def find(search_string):
    result = []
    for product_name in goods:
        if search_string.lower() in product_name.lower():
            result.append({product_name: goods[product_name]})
    return result


def amount(product_name):
    if product_name not in goods:
        return 0
    total_amount = sum(item["amount"] for item in goods[product_name])
    return total_amount


def expire():
    today = datetime.date.today()
    expired = []
    for product_name, batches in goods.items():
        for batch in batches:
            if batch["expiration_date"] and batch["expiration_date"] < today:
                expired.append({product_name: batch})
    return expired


add("Сок", 3, datetime.date(2023, 10, 1))

add_by_note("Кефир, 2, 2023-09-10")

print(find("Вареники"))


print(expire())
