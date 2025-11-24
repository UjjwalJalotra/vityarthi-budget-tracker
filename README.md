# vityarthi-budget-tracker
### 1. Menu Management

* *View Menu:* See all available items, prices, and descriptions.
* *Add Item:* Specify a category, name, price, and optional description for a new menu item.
* *Remove Item:* Remove an item by providing its category and ID.

### 2. Order Management

* *Create Order:* Log a new order by specifying the table number and a list of items with their quantities and prices. The total is calculated automatically.
* *View All Orders:* Display a comprehensive list of all historical and current orders.
* *View Pending Orders:* Filter the list to only show orders with the status 'pending'.
* *Update Order Status:* Change the status of an order (e.g., from 'pending' to 'preparing' or 'completed') using its Order ID.

### 3. Inventory Management

* *View Inventory:* Display the current stock and unit for every item.
* *Add Item:* :* Specify a category, name, price, and optional description for a new menu item.
* *Remove Item:* Remove an item by providing its category and ID.

### 2. Order Management

* *Create Order:* Log a new order by specifying the table number and a list of items with their quantities and prices. The total is calculated automatically.
* *View All Orders:* Display a comprehensive list of all historical and current orders.
* *View Pending Orders:* Filter the list to only show orders with the status 'pending'.
* *Update Order Status:* Change the status of an order (e.g., from 'pending' to 'preparing' or 'completed') using its Order ID.

### 3. Inventory Management

* *View Inventory:* Display the current stock and unit for every item.
* *Add Item:* Introduce a new stock item with its initial quantity, unit (kg/liters/pieces), and a reorder level.
* *Update Quantity:* Adjust the quantity of an existing item (use negative numbers to subtract).
* *Check Low Stock:* Run an alert check for any items whose current quantity is at or below the defined reorder level.

### 4. Staff Management

* *View Staff:* Display the full employee roster, including their role and hourly rate.
* *Add Employee:* Register a new staff member with their name, role, and hourly rate.

## 💾 Data Files
The system automatically creates and manages the following JSON files to persist data between sessions:

| File Name | Description | Class Managed By |
| :--- | :--- | :--- |
| menu.json | Stores all menu categories and items. | MenuManager |
| orders.json | Stores all past and current orders. | OrderManager |
| inventory.json | Stores current stock levels for all inventory items. | InventoryManager |
| staff.json | Stores employee records. | StaffManager |

---

## 🏗 Code Structure

The application is organized into several classes, each handling a specific domain:

* **DataManager:** Static class for handling JSON file loading and saving, providing data persistence.
* **MenuManager:** Manages the restaurant's menu.
* **OrderManager:** Handles order creation and tracking, relying on MenuManager for item details (though items are manually entered for simplicity in the current implementation).
* **InventoryManager:** Tracks stock levels and handles reorder alerts.
* **StaffManager:** Manages employee information.
* **RestaurantSystem:** The main controller class that initializes the managers and handles the primary user interaction loop.


The system automatically creates and manages the following JSON files to persist data between sessions:
