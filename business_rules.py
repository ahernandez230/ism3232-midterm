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


def needs_signoff(total: float) -> bool:
    """Return True if the total cost for an event exceeds the signoff limit, otherwise return False"""
    return total > SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    """Return True if the event requires a second chef based on the number of guests and total cost"""
    return guests > SECOND_CHEF_GUEST_LIMIT or total >= SECOND_CHEF_TOTAL_LIMIT


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Return a formatted string for an event line in the report"""
    signoff_text = "yes" if signoff else "no"
    second_chef_text = "yes" if second_chef else "no"
    return f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {second_chef_text}"


def total_booked(events: list) -> float:
    """Return the total booked amount for all events in the list"""
    running_total = 0
    for event in events:
        total = calculate_event_total (event["guest_price"], event["guests"], event["nonprofit"])
        running_total = running_total + total
    return running_total

def largest_event(events: list) -> str:
    """Return the client of the event with the largest total booked amount"""
    best_client = ""
    best_total = 0
    for event in events:
        total = calculate_event_total(event["guest_price"], event["guests"], event["nonprofit"])
        if total > best_total:
            best_total = total
            best_client = event["client"]
    return best_client
        