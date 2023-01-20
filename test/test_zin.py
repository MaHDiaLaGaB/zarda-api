import pytest
from zarda.zin import Zarda

TOTAL = 1390
NUM_USERS = 5
USERS = {"mad": 277, "max": 300, "john": 400, "fox": 121}


@pytest.fixture
def zarda_fixture():
    return Zarda(TOTAL, NUM_USERS)


def test_add(zarda_fixture):
    zarda_fixture.add_users("jack", 340)
    assert zarda_fixture.users["jack"] == 340

    zarda_fixture.delete_user("jack")
    assert zarda_fixture.users == {}


def test_calculate_spending(zarda_fixture):
    x = TOTAL / NUM_USERS
    assert zarda_fixture.calculate_spending() == x


def test_spend_each(zarda_fixture):
    zarda_fixture.users.copy(USERS)

