from typing import Dict
import math


class Zarda:
    def __init__(self, zarda_name, num_users) -> None:
        self.users = dict()
        self.zarda_name = zarda_name
        self.num_users = num_users

    def add_users(self, user: str, spent: float) -> None:
        self.users[user] = spent

    def total_spent(self):
        return sum(self.users.values())

    def calculate_spending(self) -> float:
        cost = self.total_spent() / self.num_users
        return cost

    def spent_each(self, user: str, cost: float) -> Dict:
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
        return payment

    def delete_user(self, user: str) -> None:
        del self.users[user]
