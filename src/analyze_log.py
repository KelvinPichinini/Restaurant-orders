import csv


def get_foods(orders):
    foods = set()
    for order in orders:
        if order[1] not in foods:
            foods.add(order[1])
    return foods


def get_working_days(orders):
    days = set()
    for order in orders:
        if order[2] not in days:
            days.add(order[2])
    return days


def validate_file(path: str):
    if not path.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path}'")
    try:
        file = open(path)
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path}'")


def get_orders_by_customer(orders, customer_name):
    customer_orders = {}
    for order in orders:
        if order[0] == customer_name:
            if order[1] not in customer_orders:
                customer_orders[order[1]] = 1
            else:
                customer_orders[order[1]] += 1
    if len(customer_orders.keys()) == 0:
        print(f'O clinte {customer_name} nunca fez um pedido')
    return customer_orders


def get_visit_days_of_customer(orders, customer_name):
    visiting_days = {}
    for order in orders:
        if order[0] == customer_name:
            if order[2] not in visiting_days:
                visiting_days[order[2]] = 1
            else:
                visiting_days[order[2]] += 1
    if len(visiting_days.keys()) == 0:
        print(f'O clinte {customer_name} nunca fez um pedido')
    return visiting_days


def most_ordered(orders, customer_name):
    customer_orders = get_orders_by_customer(orders, customer_name)
    return max(customer_orders, key=customer_orders.get)


def count_product_by_customer(orders, product, customer_name):
    customer_orders = get_orders_by_customer(orders, customer_name)
    if product not in customer_orders:
        print(f'O cliente {customer_name} nunca pediu {product}')
        return 0
    return customer_orders[product]


def not_ordered_food_by_customer(orders, customer_name):
    not_ordered = set()
    customer_orders = get_orders_by_customer(orders, customer_name)
    all_foods = get_foods(orders)
    for food in all_foods:
        if food not in customer_orders:
            not_ordered.add(food)
    return not_ordered


def days_not_visited_by_customer(orders, customer_name):
    not_visited = set()
    visiting_days = get_visit_days_of_customer(orders, customer_name)
    working_days = get_working_days(orders)
    for day in working_days:
        if day not in visiting_days:
            not_visited.add(day)
    return not_visited


def analyze_log(path_to_file):
    validate_file(path_to_file)
    with open(path_to_file) as file:
        log = list(csv.reader(file))
# Questions:
# Maria's most ordered food?
    maria_most_ordered = most_ordered(log, "maria")
# How many burguers arnaldo had?
    arnaldos_burguers = count_product_by_customer(log, "hamburguer", "arnaldo")
# what food Joao never ordered?
    joao_not_ordered = not_ordered_food_by_customer(log, "joao")
# which days Joao never went to the dinner?
    joao_not_visited = days_not_visited_by_customer(log, "joao")

    with open('data/mkt_campaign.txt', mode='w') as file:
        file.write(
            f'{maria_most_ordered}\n'
            f'{arnaldos_burguers}\n'
            f'{joao_not_ordered}\n'
            f'{joao_not_visited}\n'
        )
