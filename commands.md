# Terminal Record: Harvest Table Catering

## 1. Building the project
```
cd ~/Documents
mkdir ism3232-midterm
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip install --upgrade pip
pip freeze > requirements.txt
touch business_rules.py main.py commands.md README.md .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
source .venv/bin/activate
mv tests/__init.py tests/__init__.py
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
git init
git branch -M main
git remote add origin https://github.com/ahernandez230/ism3232-midterm.git
git add .gitignore requirements.txt business_rules.py main.py tests
git commit -m "Set up project structure, gitignore, and requirements"
git push -u origin main
```
## 2. The virtual environment

```
which python3
```

```
/Users/ariadnahernandez/Documents/ism3232-midterm/.venv/bin/python3
```
The path in the output goes through .venv which shows that python3 is running from my projects virtual environment and not from the computer's main python.


## 3. The project structure

```
tree -L 2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```
The __pycache__ folder is on my computer but not in my Github repository because it is listed in .gitignore and Python can create it again automatically, so it doesnt need to be stored.

## 4. Every function and test

```
rg 'def'
```

```
business_rules.py
13:def calculate_food_cost(guest_price: float, guests: int) -> float:
18:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
28:def calculate_event_total(
40:def needs_signoff(total: float) -> bool:
45:def needs_second_chef(guests: int, total: float) -> bool:
50:def format_event_line(
59:def total_booked(events: list) -> float:
70:def largest_event(events: list) -> str:

tests/test_business_rules.py
13:def test_food_cost_multiplies_price_by_guests():
17:def test_no_discount_at_24_guests():
21:def test_five_percent_discount_at_25_guests():
25:def test_five_percent_discount_at_99_guests():
29:def test_nonprofit_gets_twelve_percent_discount_at_100_guests():
33:def test_non_nonprofit_gets_five_percent_discount_at_100_guests():
37:def test_nonprofit_flag_changes_discount_at_100_guests():
43:def test_event_total_for_finch_law():
47:def test_event_total_for_garden_club():
51:def test_fee_applies_at_500():
55:def test_no_fee_just_above_500():
59:def test_no_signoff_at_exactly_2500():
63:def test_signoff_needed_right_above_2500():
67:def test_no_second_chef_needed_at_80_guests():
71:def test_second_chef_needed_at_81_guests():
75:def test_no_second_chef_needed_just_below_3000():
79:def test_second_chef_needed_at_exactly_3000():
83:def test_line_shows_no_for_both_false():
90:def test_line_shows_yes_for_both_true():
97:def test_total_booked_adds_all_event_totals():
110:def test_largest_event_tie_returns_first_in_list():
118:def test_largest_event_of_empty_list_is_empty_string():
```
business_rules.py defines 8 functions, and tests/test_business_rules.py defines 22 tests.

## 5. Which files print

```
rg -l 'print'
```

```
main.py
commands.md
```
main.py is the python file that prints, and business_rules.py is not in the list because it does not have any print functions.

## 6. The commit history

```
git log --oneline
```

```
db59002 (HEAD -> main, origin/main) Add summary lines to main.py report
7f0b5eb Add main.py event list and pre-event report lines
d8a82c0 Add total_booked and largest_event loop functions with tests
c0ad0d1 Added sign-off, second chef, and line formatter with tests
a36146d Add food cost, discount, and event total functions with tests
0b039d1 Set up project structure, gitignore, and requirements
```
There are 6 commits at the time I ran this command.
