from typing import List
import math


class Zarda:
    def __init__(self, total: int, num_users: int) -> None:
        self.total = total
        self.num_users = num_users
        self.users = {}

    def add_users(self, user: str, spent: int) -> None:
        self.users[user] = spent

    def delete_user(self, user: str) -> None:
        del self.users[user]

    def calculate_spending(self) -> float:
        cost = self.total / self.num_users
        return cost

    def spent_each(self, user: str, cost: float) -> None:
        payment = dict()
        own = self.users[user] - cost
        if math.copysign(1, own) == -1:
            print(f"{user} needs to pay {abs(own)}")
            payment[user] = f"pay {abs(own):.2f}"
        elif own == 0:
            print("The number is non-negative.")
            payment[user] = f"you are free"
        else:
            payment[user] = f"receive {own:.2f}"

