# ISM3232 Midterm: Harvest Table Catering
- Name: Ariadna Hernandez
- Version: BETA
- Date: October 25, 2026

## What This Program Does
This program was designed for the Harvest Table Catering company for their catering events. It takes a list of events (which each has a client name attatched, a price per guest, a number of guests, and whether they are nonprofit) then it calculates the total cost including discounts and discount fees. It then decides whether a manager sign-off and a second chef are needed. It then follows up with a report with one line per event and a summary. My tests are made to check that each rule works including exact limits. 

## Business Rules
- The base cost of an event is the price per guest multiplied by the number of guests.
- Events with fewer than 25 guests get no discount. Events with 25 to 99 guests get a 5% discount. Events with 100 or more guests are eligebile for a 12% discount if they are a nonprofit (5% if they are not).
- Only nonprofts get the 12% discount, any other event with 100 or more guests get only a 5% discount.  
- If the cost after the discount is $500 or less, a $75 service fee is added. 
- An event total of more than $2500 needs a manager's sigh-off.
- An event needs a second chef if it has more than 80 guests or if its total is $3,000 or more.

## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```
ruff format .
ruff check .
pytest -v
```
I wrote 22 tests.

## Files in This Repository
- `business_rules.py`: holds the eight functions that apply the business rules and the return values. 
- `main.py`: holds the list of events and prints the report and the summary.
- `commands.md`: a record of the terminal commands i types and what they printed.
- `README.md`: explains the project and how to run and test it.
- `requirements.txt`: lists the packages the project needs, including pytest and ruff.
- `.gitignore`: tells Git which files and folders to leave out.
- `tests/__init__.py` an empty file that lets the tests folder work as a package so the test can import the code.
- `tests/test_business_rules.py`: holds the tests, which check each function and the limits of the rules.

## AI Use Statement
I did not use AI for this exam. 
