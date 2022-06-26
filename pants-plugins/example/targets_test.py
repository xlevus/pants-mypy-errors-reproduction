import pytest

from example.targets import CustomTarget


@pytest.fixture
def my_target():
    return CustomTarget


def test_target(my_target):
    assert True
