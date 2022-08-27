from .analyze_log import (
    get_foods,
    get_working_days,
    get_orders_by_customer,
    get_visit_days_of_customer)


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = get_orders_by_customer(self.orders, customer)
        return max(customer_orders, key=customer_orders.get)

    def get_never_ordered_per_customer(self, customer):
        not_ordered = set()
        customer_orders = get_orders_by_customer(self.orders, customer)
        all_foods = get_foods(self.orders)
        for food in all_foods:
            if food not in customer_orders:
                not_ordered.add(food)
        return not_ordered

    def get_days_never_visited_per_customer(self, customer):
        not_visited = set()
        visiting_days = get_visit_days_of_customer(self.orders, customer)
        working_days = get_working_days(self.orders)
        for day in working_days:
            if day not in visiting_days:
                not_visited.add(day)
        return not_visited

    def get_orders_per_day(self):
        days = {}
        for order in self.orders:
            if order[2] not in days:
                days[order[2]] = 1
            else:
                days[order[2]] += 1
        return days

    def get_busiest_day(self):
        days = self.get_orders_per_day()
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = self.get_orders_per_day()
        return min(days, key=days.get)
