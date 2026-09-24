# Project Statement

## Project Title

Campus Lost & Found Management System

## Problem Statement

Students and staff can lose personal belongings on campus, while other people may find these items. Without a proper system, it can be difficult to report, search, and match lost and found items.

The Campus Lost & Found Management System provides a simple Python-based solution for managing these records.

## Objectives

The main objectives of the project are:

- Allow users to report lost items.
- Allow users to report found items.
- Store item records in an organized way.
- Allow users to search for lost and found items.
- Find possible matches between lost and found reports.
- Track the status of reported items.
- Display basic campus statistics.

## Functional Requirements

The system should:

1. Allow users to report a lost item.
2. Allow users to report a found item.
3. Display lost and found item records.
4. Search records using keywords, categories, and locations.
5. Calculate possible matches between lost and found items.
6. Allow item status to be changed between unresolved and returned.
7. Allow users to view their own reports.
8. Display basic statistics about the records.

## Non-Functional Requirements

The system should:

- Be easy to use through a simple menu-driven interface.
- Validate user input and handle invalid input safely.
- Store data reliably using a JSON file.
- Use modular Python files for easier maintenance.
- Provide useful error messages instead of crashing.
- Process normal searches and matching operations efficiently.

## Major Modules

### 1. Item Management

Handles reporting and viewing lost and found items.

### 2. Search and Matching

Allows users to search records and identifies possible matches using a rule-based scoring system.

### 3. Reports and Records

Handles user reports, item status, statistics, and JSON-based data storage.

## Technologies Used

- Python
- JSON
- Python `unittest`
- Git and GitHub

## Expected Outcome

The final system will provide a working command-line application that helps manage campus lost and found records in an organized way.

The project demonstrates practical use of Python programming concepts including functions, modules, file handling, validation, exception handling, data processing, and testing.