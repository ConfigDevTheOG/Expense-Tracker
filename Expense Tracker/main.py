import json as js
import module as mod
import datetime

#------------------------------------------------------------------------------Main Program---------------------------------------------------------------------------------------------
mod.start()

FILE_PATH_BUDGET = "E:\\Programming\\Python\\Projects\\Active\\Expense Tracker\\budget.json"

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

def check_budget(expense, variable):
    global difference

    try:
        with open(FILE_PATH_BUDGET, "r") as file:
            data = js.load(file)["budget"]

        if variable not in data:
            return False

        budget = int(data[variable])

        if budget < expense:
            difference = expense - budget
            return True, difference

        return False

    except FileNotFoundError:
        print("File not found!")

    except PermissionError:
        print("Permission denied!")

    except UnicodeDecodeError:
        print("Encoding issue!")

    except js.JSONDecodeError:
        print("Could not decode JSON!")

    except TypeError:
        print("Invalid data type in JSON!")

    return False

def budget():
    for i in budget_database.keys():
     if i not in ["income", "total_expenses", "monthly_balance"]:
            while True:
               try:
                  avg_budget = float(input(f"Enter estimated monthly budget of {i}: "))
                  budget_database[i] = avg_budget
                  break

               except ValueError:
                  print("Please enter numbers")

     elif i != "total_expenses" and i != "monthly_balance":
            while True:
               try:
                  avg_income = float(input("Enter estimated monthly income: "))
                  budget_database[i] = avg_income
                  break

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
         if i not in ["date", "total_expenses", "monthly_balance", "income"]:
            while True:
               try:
                  expense = float(input(f"Enter the expense of {i} in {month}: "))
                  difference = check_budget(expense, i)

                  if difference:
                     print(f"Warning: Expense of {i} exceeds the budget by {difference}!")
                  
                  database[i] = expense
                  break

               except ValueError:
                  print("Please enter numbers")
         
         elif i == "income":
            while True:
               try:
                  income = float(input(f"Enter your income of {month}: "))
                  database[i] = income
                  break

               except ValueError:
                  print("Please enter numbers")

         elif i == "date":
            database[i] = datetime.date.today().strftime("%Y-%m-%d")
      break

   print("Adding expenses and calculating totals...")
   
   total = 0
    
   for key, value in database.items():
    if key not in ["income", "date", "monthly_balance", "total_expenses"]:
      if isinstance(value, (int, float)):
         total += value
         if total > database["income"]:
            print(f"Warning: Total expenses exceed income by {total - database['income']}!")
   
   balance = database['income'] - total

   database["monthly_balance"] = balance
   database["total_expenses"] = total
  
   mod.add_month(month, database) 
   
   print("Expenses added successfully")

#---------------------------------------------------------------------------------Main loop-----------------------------------------------------------------------------------------

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
