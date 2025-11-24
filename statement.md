Data Persistence: The application uses the json library to save and load the budget data to/from a file named budget_data.json.

load_data(): Loads the total_budget and a list of expenses from the JSON file. If the file is not found or corrupted, it starts a new budget.

save_data(total_budget, expenses_list): Saves the current total_budget and aggregates the expenses by category into a dictionary before writing them to the JSON file.

Budget Management:

set_budget(expenses_list): Prompts the user to enter their total monthly budget, ensuring the input is a valid positive number.

Expense Tracking:

add_expense(expenses_list): Prompts the user for an expense category and amount, validating that the amount is positive. It adds the new expense as a [category, amount] list to the expenses_list.

Status Reporting:

view_status(total_budget, expenses_list): Calculates and displays a detailed summary of the budget status.

It shows the Total Budget and Total Spending.

It calculates and displays the Remaining Balance, providing a status message (e.g., "Good job! 🎉" or "🛑 OVER BUDGET! 😟").

It provides a breakdown of all spending, summarizing the total amount spent for each expense Category.

Main Application Flow:

main_menu(): Manages the command-line interface, providing options to:

Set/Change Total Budget.

Add New Expense.

View Budget Status/Breakdown.

Exit.
