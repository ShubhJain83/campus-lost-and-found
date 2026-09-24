# Campus Lost & Found Management System

## 1. Project Overview

The Campus Lost & Found Management System is a Python-based command-line application designed to help students report and manage lost and found items on a college campus.

The system stores item reports, allows users to search records, finds possible matches between lost and found items, manages item status, and displays basic campus statistics.

The project uses Python and JSON file storage without requiring external libraries.

---

## 2. Problem Statement

Students can lose personal belongings such as wallets, bags, books, documents, keys, and electronic items on campus.

Managing these items manually can make it difficult to find the correct lost or found record.

This project provides a simple digital system where users can report lost and found items and use search and matching features to identify possible matches.

---

## 3. Objectives

The main objectives of the project are:

- To provide a simple system for reporting lost items.
- To provide a system for reporting found items.
- To allow users to search item records.
- To identify possible matches between lost and found items.
- To maintain item status such as unresolved or returned.
- To provide basic statistics about campus lost and found records.
- To practice Python programming, modular design, validation, file handling, and testing.

---

## 4. Features

### Lost Item Management

- Report a lost item.
- View all lost item reports.
- Store item name, category, description, location, date, and contact information.

### Found Item Management

- Report a found item.
- View all found item reports.
- Store details of found items.

### Search System

Users can search records using:

- Keyword
- Category
- Location

### Matching System

The system calculates a match score between lost and found items using:

- Item name
- Category
- Location
- Date
- Description

A possible match is displayed when the score reaches the defined threshold.

### Status Management

Users can change an item's status between:

- Unresolved
- Returned

### Reports and Statistics

The system displays:

- Total reports
- Lost reports
- Found reports
- Returned items
- Unresolved items
- Items by category
- Reports by location

---

## 5. Technology Used

- Python 3
- JSON
- Python `unittest`
- Python standard library
- Git and GitHub

No external Python packages are required.

---

## 6. Project Structure

```text
campus-lost-and-found/
│
├── main.py
├── lost_items.py
├── found_items.py
├── matching.py
├── reports.py
├── storage.py
├── validators.py
├── utils.py
│
├── data/
│   └── records.json
│
├── tests/
│   ├── __init__.py
│   └── test_project.py
│
├── README.md
├── statement.md
└── requirements.txt

---

## 7. Module Description

| File | Purpose |
|---|---|
| `main.py` | Main menu and application flow |
| `lost_items.py` | Lost item reporting and viewing |
| `found_items.py` | Found item reporting and viewing |
| `matching.py` | Match score calculation |
| `reports.py` | Statistics and user reports |
| `storage.py` | JSON data storage |
| `validators.py` | Input validation |
| `utils.py` | Common utility functions |
| `test_project.py` | Automated unit tests |

---

## 8. How to Run the Project

### Step 1: Install Python

Install Python 3 if it is not already installed.

### Step 2: Open the Project Folder

Open a terminal inside the project folder.

### Step 3: Run the Application

```bash
python main.py

---

## 9. How to Run Tests

The project uses Python's built-in `unittest` framework.

Run:

```bash
python -m unittest discover -s tests -v

---

## 10. Data Storage

The application stores records in:

```text
data/records.json

---

## 11. Matching Logic

The matching system uses a rule-based scoring method.

The score considers:

| Factor | Maximum Score |
|---|---:|
| Item name | 40 |
| Category | 20 |
| Location | 20 |
| Date | 10 |
| Description | 10 |
| **Total** | **100** |

Items from different categories are not treated as possible matches.

The system displays possible matches when the score reaches the configured threshold.

---

## 12. Input Validation

The system validates user input before storing records.

Validation includes:

- Empty fields
- Date format
- Contact information
- Item category
- Menu choices

Invalid input produces an error message instead of crashing the program.

---

## 13. Testing

The project contains automated unit tests using Python's `unittest` module.

Current result:

```text
Ran 4 tests
OK

---

## 14. Limitations

- The system currently uses a command-line interface.
- Data is stored locally in a JSON file.
- Users need to enter correct item details for better matching results.
- The matching system uses rule-based scoring and does not use machine learning.

---

## 15. Future Enhancements

Possible improvements for future versions include:

- Adding a graphical user interface (GUI).
- Adding user login and authentication.
- Using a database instead of a JSON file.
- Improving the matching algorithm.
- Adding email or notification support.
- Adding an admin dashboard for campus staff.

---

## 16. Conclusion

The Campus Lost & Found Management System provides a simple way to report, search, and manage lost and found items on a campus.

The project demonstrates Python programming concepts such as functions, modules, file handling, JSON storage, input validation, exception handling, searching, data processing, and unit testing.

The matching system also provides a basic rule-based method to identify possible matches between lost and found items.