# FinTrack

FinTrack is a personal finance manager built with Python. It helps you manage and analyze your financial transactions, set budgets, and visualize your spending habits over time. This project involves data handling, file I/O, data visualization, web scraping, and creating a graphical user interface (GUI).

## Features

- **Transaction Management**: Input, update, and delete financial transactions.
- **Data Validation**: Ensure inputs are correctly formatted and valid.
- **Data Storage**: Store data in CSV files and SQLite database.
- **Data Analysis**: Summarize income, expenses, and balance; analyze spending by category.
- **Data Visualization**: Create bar charts, pie charts, and time series plots.
- **Budgeting**: Set and track monthly budgets for different categories.
- **Web Scraping (Optional)**: Fetch external data such as exchange rates or stock prices.
- **Graphical User Interface (GUI)**: Provide a user-friendly interface for managing finances.

## Project Structure


### Directory and File Descriptions

- **`data/`**: Contains data files used by the project. The `transactions.csv` file stores financial transactions.
- **`db/`**: Contains the SQLite database file `finance.db` for storing and managing financial data.
- **`docs/`**: Includes project documentation, such as this `README.md` file.
- **`src/`**: Contains source code files for the project.
  - **`analysis.py`**: Functions for analyzing financial data.
  - **`database.py`**: Functions for handling database operations.
  - **`gui.py`**: Code for the Tkinter graphical user interface.
  - **`main.py`**: Main script to run the application.
  - **`scraping.py`**: Functions for web scraping (optional).
  - **`transactions.py`**: Functions for managing transactions.
  - **`visualization.py`**: Functions for visualizing data.
- **`tests/`**: Contains unit tests for the project. The `test_transactions.py` file includes tests for transaction management.
- **`requirements.txt`**: Lists the Python packages and their versions required for the project.
- **`LICENSE`**: Contains the license information for the project.

This structure helps in organizing the project effectively, making it easier to navigate and maintain.


# FinTrack Project Schedule

## Week 1: Project Setup and Basic Structure
| **Day** | **Tasks** | **Skills and Concepts Learned** |
|---------|-----------|---------------------------------|
| 1-2     | Project setup, GitHub repository            | Development environment setup, version control |
| 3-4     | Basic input/output (transactions to CSV)    | File I/O, user input handling |
| 5-7     | Data validation, read/display CSV           | Data validation, CSV manipulation |

## Week 2: Data Management with Pandas
| **Day** | **Tasks** | **Skills and Concepts Learned** |
|---------|-----------|---------------------------------|
| 8-10    | Introduce Pandas                            | Basics of Pandas, DataFrame handling |
| 11-14   | Data manipulation with Pandas               | Adding, updating, deleting data in DataFrames |

## Week 3: Data Analysis
| **Day** | **Tasks** | **Skills and Concepts Learned** |
|---------|-----------|---------------------------------|
| 15-17   | Summarize data (totals, categories)         | Data summarization, aggregation |
| 18-21   | Data visualization (matplotlib, seaborn)    | Creating plots, data visualization |

## Week 4: Advanced Data Analysis and Visualization
| **Day** | **Tasks** | **Skills and Concepts Learned** |
|---------|-----------|---------------------------------|
| 22-25   | Time series analysis                        | Time series data handling, trend analysis |
| 26-28   | Budgeting features                          | Budgeting, comparing actual vs. planned data |

## Week 5: Web Scraping (Optional)
| **Day** | **Tasks** | **Skills and Concepts Learned** |
|---------|-----------|---------------------------------|
| 29-32   | Introduction to web scraping                | Basics of web scraping, using requests and BeautifulSoup |
| 33-35   | Integrate web scraping                      | Fetching and storing external data |

## Week 6: Database Management
| **Day** | **Tasks** | **Skills and Concepts Learned** |
|---------|-----------|---------------------------------|
| 36-39   | Introduction to SQLite                      | Basics of SQLite, database creation |
| 40-42   | Database integration                        | CRUD operations with SQLite |

## Week 7: GUI Development
| **Day** | **Tasks** | **Skills and Concepts Learned** |
|---------|-----------|---------------------------------|
| 43-46   | Introduction to Tkinter                     | Basics of Tkinter, GUI development |
| 47-49   | Display data in GUI                         | GUI data display, integration with backend |

## Week 8: Finalizing and Testing
| **Day** | **Tasks** | **Skills and Concepts Learned** |
|---------|-----------|---------------------------------|
| 50-53   | Testing                                    | Writing unit tests, debugging |
| 54-56   | Documentation                              | Writing project documentation |
| 57-60   | Final touches and deployment               | Finalizing project, creating executable or deployment |

## Daily Routine
- **Day 1-2 hours**: Follow the tasks assigned for the day.
- **Take Notes**: Keep notes of what you learn and any issues you encounter.
- **Review Code**: Spend the last 15-20 minutes reviewing your code and making improvements.

This structured schedule will help you systematically improve your Python programming skills while building a comprehensive personal finance manager project. You can adjust the plan as needed based on your progress and interests.

## Acknowledgements

- **[pandas](https://pandas.pydata.org/)**: For powerful data manipulation and analysis.
- **[matplotlib](https://matplotlib.org/)**: For creating static, animated, and interactive visualizations in Python.
- **[seaborn](https://seaborn.pydata.org/)**: For making statistical data visualization easier with a high-level interface.
- **[requests](https://requests.readthedocs.io/)**: For simplifying HTTP requests and web scraping.
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)**: For parsing HTML and XML documents, and web scraping.
- **[sqlite3](https://docs.python.org/3/library/sqlite3.html)**: For lightweight, disk-based database management.
- **[tkinter](https://docs.python.org/3/library/tkinter.html)**: For building graphical user interfaces in Python.

Thank you to the open-source community for providing these valuable tools and libraries!


# FinTrack Project Tasks: Features

## Feature 1: Transaction Management

### Task 1: Input Transactions
- **Objective**: Develop functionality to add new financial transactions.
- **Details**: 
  - Create forms or input fields for date, description, amount, and category.
  - Validate input data to ensure correctness.
  - Save transactions to a CSV file and/or SQLite database.

### Task 2: Update Transactions
- **Objective**: Implement functionality to update existing transactions.
- **Details**: 
  - Provide a way to select and edit existing transactions.
  - Ensure changes are validated and correctly updated in the CSV file and/or SQLite database.

### Task 3: Delete Transactions
- **Objective**: Add functionality to delete transactions.
- **Details**: 
  - Provide a method to select and remove transactions.
  - Ensure transactions are deleted from both the CSV file and/or SQLite database.

## Feature 2: Data Validation

### Task 1: Input Validation
- **Objective**: Ensure that all user inputs are correctly formatted and valid.
- **Details**: 
  - Implement checks for valid date formats, numeric values, and non-empty fields.
  - Provide user feedback for incorrect inputs.

### Task 2: Error Handling
- **Objective**: Handle errors gracefully during data entry and processing.
- **Details**: 
  - Implement error messages and logging for invalid inputs and file/database operations.

## Feature 3: Data Storage

### Task 1: CSV File Storage
- **Objective**: Store financial transactions in a CSV file.
- **Details**: 
  - Design the CSV format for storing transaction data.
  - Implement reading from and writing to the CSV file.

### Task 2: SQLite Database Storage
- **Objective**: Store financial transactions in an SQLite database.
- **Details**: 
  - Design the database schema for transactions.
  - Implement CRUD operations to interact with the database.

## Feature 4: Data Analysis

### Task 1: Summarize Data
- **Objective**: Generate summaries of financial data.
- **Details**: 
  - Calculate totals, categorize expenses, and summarize income and expenses.
  - Provide summary reports or tables.

### Task 2: Analyze Spending
- **Objective**: Analyze spending patterns and trends.
- **Details**: 
  - Group data by category and time period.
  - Calculate trends and compare against budgets.

## Feature 5: Data Visualization

### Task 1: Create Charts
- **Objective**: Develop visualizations for financial data.
- **Details**: 
  - Implement bar charts, pie charts, and line graphs using `matplotlib` and `seaborn`.
  - Display summaries of spending, income, and budget comparisons.

### Task 2: Time Series Plots
- **Objective**: Visualize spending trends over time.
- **Details**: 
  - Create line plots to show changes in financial data over time.
  - Implement features to zoom and interact with time series data.

## Feature 6: Budgeting

### Task 1: Set Budgets
- **Objective**: Allow users to set and track budgets for various categories.
- **Details**: 
  - Create forms for entering and updating budget limits.
  - Store budget data and compare actual spending against the budget.

### Task 2: Track Budget Performance
- **Objective**: Monitor and report on budget performance.
- **Details**: 
  - Generate reports or alerts when spending exceeds budget limits.
  - Provide visualizations comparing budgeted vs. actual spending.

## Feature 7: Web Scraping (Optional)

### Task 1: Fetch External Data
- **Objective**: Retrieve external data such as exchange rates or stock prices.
- **Details**: 
  - Implement web scraping using `requests` and `BeautifulSoup`.
  - Parse and store the fetched data.

### Task 2: Integrate External Data
- **Objective**: Use external data to enhance financial tracking.
- **Details**: 
  - Incorporate exchange rates or stock prices into financial reports or visualizations.

## Feature 8: Graphical User Interface (GUI)

### Task 1: Design GUI
- **Objective**: Develop a user-friendly graphical interface using Tkinter.
- **Details**: 
  - Create windows, forms, and controls for managing transactions and displaying data.

### Task 2: Integrate Functionality
- **Objective**: Connect GUI elements with backend functionality.
- **Details**: 
  - Implement event handlers for user actions such as adding, updating, and deleting transactions.
  - Display data and visualizations within the GUI.

## Final Tasks

### Task 1: Testing
- **Objective**: Ensure all features work correctly and fix any issues.
- **Details**: 
  - Write and run unit tests for core functionalities.
  - Perform manual testing to verify feature integration and usability.

### Task 2: Documentation
- **Objective**: Document the project and its features.
- **Details**: 
  - Write comprehensive documentation including setup instructions, usage guides, and feature descriptions.

### Task 3: Deployment
- **Objective**: Prepare the project for deployment or distribution.
- **Details**: 
  - Create executable files or set up hosting if applicable.
  - Ensure all dependencies and configurations are included.

This task list covers the implementation of the core features for the FinTrack project and provides a structured approach to building and refining the application.

