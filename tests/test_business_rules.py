from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
)


def test_food_cost_multiplies_price_by_guests():
    assert round(calculate_food_cost(10.00, 5), 2) == 50.00


def test_no_discount_at_24_guests():
    assert get_event_discount(24) == 0.0


def test_five_percent_discount_at_25_guests():
    assert get_event_discount(25) == 0.05


def test_five_percent_discount_at_99_guests():
    assert get_event_discount(99) == 0.05


def test_nonprofit_gets_twelve_percent_discount_at_100_guests():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_non_nonprofit_gets_five_percent_discount_at_100_guests():
    assert get_event_discount(100, nonprofit=False) == 0.05


def test_nonprofit_flag_changes_discount_at_100_guests():
    assert get_event_discount(100, nonprofit=True) != get_event_discount(
        100, nonprofit=False
    )


def test_event_total_for_finch_law():
    assert round(calculate_event_total(18.00, 20, nonprofit=False), 2) == 435.00


def test_event_total_for_garden_club():
    assert round(calculate_event_total(22.00, 40, nonprofit=True), 2) == 836.00


def test_fee_applies_at_500():
    assert round(calculate_event_total(500.00, 1, nonprofit=False), 2) == 575.00


def test_no_fee_just_above_500():
    assert round(calculate_event_total(500.01, 1, nonprofit=False), 2) == 500.01
