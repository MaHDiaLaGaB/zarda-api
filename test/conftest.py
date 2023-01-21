import pytest
from zarda.zin import Zarda
from .constants import NUM_USERS, TOTAL


@pytest.fixture
def zarda():
    return Zarda(TOTAL, NUM_USERS)
