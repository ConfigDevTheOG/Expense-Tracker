import json

def start():
    months = [
        "january", "february", "march", "april",
        "may", "june", "july", "august",
        "september", "october", "november", "december"
    ]

    template = {
        "date": "",
        "income": 0,
        "rent": 0,
        "groceries": 0,
        "electricity": 0,
        "education": 0,
        "basic_needs": 0,
        "entertainment": 0,
        "child_needs": 0,
        "extra_expenses": 0,
        "shopping": 0,
        "healthcare": 0,
        "insurance": 0,
        "total_expenses": 0,
        "monthly_balance": 0
    }



    try:
        with open("E:\\Programming\\Python\\Projects\\Active\\Expense Tracker\\ExpenseTracker.json", "r") as file:
            save = json.load(file)
    except FileNotFoundError:
        budget = {month: template.copy() for month in months}

        with open("E:\\Programming\\Python\\Projects\\Active\\Expense Tracker\\ExpenseTracker.json", "w") as file:
            json.dump(budget, file, indent=4)

if __name__ == "__main__":
     start()
