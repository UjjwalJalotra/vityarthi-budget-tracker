import json

DATA_FILE = "budget_data.json"


def load_data():
    """Loads budget and expenses from the JSON file into a tuple (budget, expenses_list)."""
    total_budget = 0.0
    expenses_list = []
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            
            # 1. Load Budget
            total_budget = float(data.get('total_budget', 0.0))

            saved_expenses_dict = data.get('expenses', {})
            for category, amount in saved_expenses_dict.items():
                expenses_list.append([category, amount])
                
        print(f"✅ Data loaded successfully from {DATA_FILE}.")
    except FileNotFoundError:
        print(f"No existing data file found ({DATA_FILE}). Starting a new budget.")
    except (json.JSONDecodeError, TypeError) as e:
        print(f"⚠️ Error loading data. Starting with a fresh budget. ({e})")


    return total_budget, expenses_list

def save_data(total_budget, expenses_list):
    """Saves the budget and expenses list to the JSON file."""
    

    expenses_dict_to_save = {}
    for category, amount in expenses_list:
  
        expenses_dict_to_save[category] = expenses_dict_to_save.get(category, 0) + amount

    data_to_save = {
        'total_budget': total_budget,
        'expenses': expenses_dict_to_save
    }
    
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data_to_save, f, indent=4)
        print(f"\n💾 Data saved to {DATA_FILE}.")
    except Exception as e:
        print(f"🛑 Error saving data: {e}")


def set_budget(expenses_list):
    """Sets the total monthly budget and returns the new budget value."""
    while True:
        try:
            amount = float(input("Enter your total monthly budget: Rs"))
            if amount < 0:
                print("Budget must be a positive number.")
                continue
            
            new_budget = amount
            print(f"\n✅ Total budget set to: Rs.{new_budget:.2f}")
            return new_budget
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

def add_expense(expenses_list):
    """Adds an expense to the expenses list (which is modified in place)."""
    while True:
        try:
            category = input("\nEnter expense category: ").strip().capitalize()
            if not category:
                print("Category cannot be empty.")
                continue

            amount = float(input(f"Enter amount spent on {category}: Rs."))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue


            expenses_list.append([category, amount])

            print(f"\n✅ Added Rs.{amount:.2f} to {category}.")
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

def view_status(total_budget, expenses_list):
    """Displays the budget status using the list data."""
    print("\n" + "="*30)
    print("      💸 BUDGET STATUS 📊")
    print("="*30)

    if total_budget == 0.0:
        print("🛑 Please set your total budget first.")
        return

    total_spending = 0.0
    category_summary = {} 

    for category, amount in expenses_list:
        total_spending += amount
        category_summary[category] = category_summary.get(category, 0) + amount

    remaining_balance = total_budget - total_spending
    
    # Display summary
    print(f"**Total Budget:** Rs.{total_budget:.2f}")
    print(f"**Total Spending:** Rs.{total_spending:.2f}")
    
    # Display balance with status
    if remaining_balance >= 0:
        print(f"**Remaining Balance:** Rs.{remaining_balance:.2f} (Good job! 🎉)")
    else:
        over_by = abs(remaining_balance)
        print(f"**Remaining Balance:** -Rs{over_by:.2f} (🛑 OVER BUDGET! 😟)")

    print("-" * 30)

    # Display detailed breakdown from the temporary dictionary
    if expenses_list:
        print("\n**Expense Breakdown by Category:**")
        for category, amount in sorted(category_summary.items()):
            print(f"- {category}: Rs.{amount:.2f}")
    else:
        print("\nNo expenses recorded yet.")
    
    print("="*30)



def main_menu():
    """Manages the application flow and holds the state."""
    

    total_budget, expenses_list = load_data()
    
    if total_budget == 0.0:
        print("\nWelcome to the Simple Python Budget Tracker!")
        result = set_budget(expenses_list)
        if result is not None:
            total_budget = result
            save_data(total_budget, expenses_list) # Save initial budget

    while True:
        print("\n" + "~"*30)
        print("   💰 Expense Tracker Menu 📝")
        print("~"*30)
        print("1. Set/Change Total Budget")
        print("2. Add New Expense")
        print("3. View Budget Status/Breakdown")
        print("4. Exit")
        print("~"*30)

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            new_budget = set_budget(expenses_list)
            if new_budget is not None:
                total_budget = new_budget
                save_data(total_budget, expenses_list)
        elif choice == '2':
            add_expense(expenses_list)
            save_data(total_budget, expenses_list) # Save data after modifying list
        elif choice == '3':
            view_status(total_budget, expenses_list)
        elif choice == '4':
            print("\nThank you for using the Expense Tracker! Goodbye. 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()