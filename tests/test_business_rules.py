from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    needs_second_chef,
    needs_signoff,
    total_booked,
    largest_event,
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


def test_no_signoff_at_exactly_2500():
    assert needs_signoff(2500) is False


def test_signoff_needed_right_above_2500():
    assert needs_signoff(2500.01) is True


def test_no_second_chef_needed_at_80_guests():
    assert needs_second_chef(80, 1000) is False


def test_second_chef_needed_at_81_guests():
    assert needs_second_chef(81, 1000) is True


def test_no_second_chef_needed_just_below_3000():
    assert needs_second_chef(10, 2999.99) is False


def test_second_chef_needed_at_exactly_3000():
    assert needs_second_chef(10, 3000.00) is True


def test_line_shows_no_for_both_false():
    assert (
        format_event_line("Finch Law", 435.00, False, False)
        == "Finch Law: $435.00 | sign-off: no | second chef: no"
    )


def test_line_shows_yes_for_both_true():
    assert (
        format_event_line("Hilltop Gym", 3420.00, True, True)
        == "Hilltop Gym: $3420.00 | sign-off: yes | second chef: yes"
    )


def test_total_booked_adds_all_event_totals():
    events = [
        {"client": "Finch Law", "guest_price": 18.00, "guests": 20, "nonprofit": False},
        {"client": "Garden Club", "guest_price": 22.00, "guests": 40, "nonprofit": True},
    ]
    assert round(total_booked(events), 2) == 1271.00

def test_largest_event_tie_returns_first_in_list():
    events = [
       {"client": "First", "guest_price": 10.00, "guests": 100, "nonprofit": False},
         {"client": "Second", "guest_price": 20.00, "guests": 50, "nonprofit": False},
    ]
    assert largest_event(events) == "First"

def test_largest_event_of_empty_list_is_empty_string():
    assert largest_event([ ]) == ""
