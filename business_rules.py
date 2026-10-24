# Constants
SMALL_DISCOUNT_MIN_GUESTS = 25
LARGE_DISCOUNT_MIN_GUESTS = 100
STANDARD_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12
SERVICE_FEE_LIMIT = 500
SERVICE_FEE = 75
SIGNOFF_LIMIT = 2500
SECOND_CHEF_GUEST_LIMIT = 80
SECOND_CHEF_TOTAL_LIMIT = 3000


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Return the total food cost for an event based on the guest price and number of guests"""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate for an event based on the number of guests and whether the client is a nonprofit"""
    if guests < SMALL_DISCOUNT_MIN_GUESTS:
        return 0.0
    elif guests >= LARGE_DISCOUNT_MIN_GUESTS and nonprofit:
        return NONPROFIT_DISCOUNT
    else:
        return STANDARD_DISCOUNT


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Return the total cost for an event based on the guest price, number of guests, and whether the client is a nonprofit"""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    total = food_cost - (food_cost * discount)
    if total <= SERVICE_FEE_LIMIT:
        total += SERVICE_FEE
    return total
