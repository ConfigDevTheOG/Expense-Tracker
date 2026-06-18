import json as js
import module as mod

#--------------------------------------------------------------------Main Program---------------------------------------------------------------------------------
mod.start()

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

database = {
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

def main():
   print("Starting Tracker...")

if __name__ == "__main__":
   main()

def budget():
    for i in budget_database.keys():
     if i not in ["income", "total_expenses", "monthly_balance"]:
            while True:
               try:
                  avg_budget = float(input(f"\nEnter estimated monthly budget of {i}: "))
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

def expenses():
   
   while True:

      month = input("Enter a month to which you want to add expenses: ").lower()

      
      if month not in [ "january", "february", "march", "april","may", "june", "july", "august", "september", "october", "november", "december"]:
         print("Please enter a month in full form")
         continue
         
      for i in database.keys():
            try:
               if i not in ["total_expenses", "monthly_balance", "date"]:
                  value = float(input(f"Please enter the value of {i} in {month}: "))
                  database[i] = value
                  break

            except ValueError:
               print("Please enter a number")
      break

   print("Adding expenses and calculating totals...")
   
   total = 0
   for i in database.values():
      total += i
   
   balance = database['income'] - total

   database["monthly_balance"] = balance
   database["total_expenses"] = total
  
   mod.add_month(month, database) 
   
   print("Expenses added successfully")

while True:
   try:
      operation = int(input("""
                            
      1. Enter monthly budget of the following year
      2. Enter expenses of a month
      3. View expenses
      4. Exit
                           
      Please enter the number corresponded with the desired action: """))

      if operation == 4:
         break 

      elif operation == 1:
         budget()

      elif operation == 2:
         expenses()

   except ValueError:
      print("\nPlease enter a number Please enter the number corresponded with the desired action")
