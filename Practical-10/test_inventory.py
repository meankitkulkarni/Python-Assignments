import pytest
from inventory import apply_discount, calculate_total_price, check_stock


def test_calculate_total_price_valid():
    assert calculate_total_price(200, 5) == 1000


def test_calculate_total_price_negative_price():
    with pytest.raises(ValueError):
        calculate_total_price(-50, 2)


def test_calculate_total_price_zero_quantity():
    with pytest.raises(ValueError):
        calculate_total_price(100, 0)


def test_apply_discount_valid():
    assert apply_discount(1000, 10) == 900


def test_apply_discount_invalid_percent():
    with pytest.raises(ValueError):
        apply_discount(1000, 120)


def test_check_stock_sufficient():
    assert check_stock(20, 5) is True


def test_check_stock_insufficient():
    assert check_stock(3, 5) is False


def test_check_stock_negative_available():
    with pytest.raises(ValueError):
        check_stock(-5, 2)
