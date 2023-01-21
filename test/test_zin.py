from .constants import USERS, TOTAL, NUM_USERS


def test_add(zarda):
    zarda.add_users("jack", 340)
    assert zarda.users["jack"] == 340

    zarda.delete_user("jack")
    assert zarda.users == {}


def test_calculate_spending(zarda):
    x = TOTAL / NUM_USERS
    assert zarda.calculate_spending() == x


def test_spend_each(zarda):
    payments = dict()
    for k, v in USERS.items():
        zarda.add_users(k, v)
        payments.update(zarda.spent_each(k, zarda.calculate_spending()))
    print(payments)
    assert len(payments) == 5
    assert payments["mad"] == "pay 1.00"





