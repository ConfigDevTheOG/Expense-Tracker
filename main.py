import json as js

#--------------------------------------------------------------------Main Program---------------------------------------------------------------------------------

budget_database = {
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

data+


def budget():
    for i in budget_database.keys():
     if i not in ["income", "total_expenses", "monthly_balance"]:
            while True:
               try:
                  avg_budget = float(input(f"Enter estimated monthly budget of {i}: "))
                  budget_database[i] = avg_budget

               except ValueError:
                  print("Please enter numbers")

     elif i != "total_expenses" and i != "monthly_balance":
            while True:
               try:
                  avg_income = float(input("Enter estimated monthly income: "))
                  budget_database[i] = avg_income

               except ValueError:
                  print("Please enter a number")

     elif i == "total_expenses": 

      
        total = 0 
        for k, v in budget_database.items():
           if k not in ["income", "total_expenses", "monthly_balance"]:
              total += v
        budget_database["total_expenses"]  = total

     else:
        balance = budget_database["income"] - budget_database["total_expenses"]
        budget_database["monthly_balance"] =  balance

    with open("E:\\Programming\\Python\\Projects\\Active\\Expense Tracker\\budget.json", "w") as file:
       js.dump({"budget": budget_database}, file, indent=4)
        
budget()

for k, v in budget_database.items():
   print(f"{k}:{v}")
