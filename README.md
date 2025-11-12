**📊 Data Visualization and Inventory Management System (Python)**
**📝 Overview**
This project is a Python-based data management and visualization system designed to handle and analyze data for a Game Sales Store (or similar retail system).
It provides interactive menu-driven options to:
- Manage inventory, sales, and employee data.
- Add, update, delete, and search records.
- Perform sorting and filtering operations.
- Generate data visualizations using Matplotlib.

The system reads and writes data from CSV files (Inventory.csv, Book2.csv, Employees.csv, Sales.csv) and provides simple text-based menus for user interaction.

**🚀 Features**
**🔹 Inventory Management**
- View, add, delete, modify, and search game/product records.
- Sort and filter inventory data.
- Calculate total stock value.
- Generate bar charts and line charts for price and stock analysis.

**🔹 Sales Management**
- Manage customer sales records.
- Add, update, delete, or search sales data.
- Filter sales by payment method.
- Generate visual comparisons of total amounts using bar and line charts.

**🔹 Employee Management**
- View, add, modify, and delete employee data.
- Sort and filter employee lists.
- Display total employee count.
- Visualize salary distributions using bar and line charts.

**🛠️ Technologies Used**
- Programming Language: Python
- Libraries:
  - pandas — For data manipulation and file I/O
  - matplotlib — For plotting charts and graphs
- Data Storage: CSV files (Inventory.csv, Book2.csv, Employees.csv, Sales.csv)

**📂 Project Structure**
📦 Data_Visualisation_Using_Python
│
├── Data_Visualisation_Using_Python.py     # Main program file
├── Inventory.csv                           # Inventory data
├── Book2.csv                               # Game data file
├── Employees.csv                           # Employee records
├── Sales.csv                               # Sales transactions
├── README.md                               # Documentation (this file)

**▶️ How to Run the Project**
Step 1: Install Dependencies
Make sure Python is installed (preferably Python 3.8+).  
Install required libraries:

pip install pandas matplotlib

Step 2: Prepare Data Files
Ensure the following CSV files exist in the same directory:
- Inventory.csv
- Book2.csv
- Employees.csv
- Sales.csv

If they don’t exist, create blank CSV files with appropriate headers or use sample data.

Step 3: Run the Program
python Data_Visualisation_Using_Python.py

The program opens a menu-driven console interface where you can:
- Manage books/inventory
- Manage sales data
- Manage employee records
- Exit safely

**📈 Sample Visualizations**
The system uses Matplotlib to generate the following graphs:
- Bar Chart – Compare product prices or employee salaries.
- Line Chart – Visualize stock or sales trends over time.

Example:
df[['Product Name','Total Amount']].plot(kind='bar', color='blue')
plt.title("Comparison of Product Prices")
plt.show()

**🔒 Data Handling and Safety**
- All CRUD operations (Create, Read, Update, Delete) are performed on CSVs using pandas.
- Data is automatically saved back to the corresponding CSV after each operation.
- Includes basic validation and menu options to prevent accidental data loss.

**💡 Advantages**
✅ User-friendly menu interface  
✅ Real-time data visualization  
✅ Simple CSV-based storage — no need for external databases  
✅ Easy customization for different datasets  

**⚙️ Future Enhancements**
- Add GUI using Tkinter or PyQt  
- Integrate database (MySQL or SQLite) instead of CSV  
- Include report generation (PDF or Excel)  
- Add more advanced visualization dashboards (using Seaborn or Plotly)

**👨‍💻 Author**
Hardik (PRO_CODER90)  
📧 hardikjain5488@gmail.com  
💼 GitHub: https://github.com/PRO-CODER90  

