# FastBox Delivery System

This project is a small Python-based delivery management system for FastBox.

The main idea of the project is to assign packages to delivery agents based on their location, calculate the delivery distance, and generate a few reports from the results.

I kept the implementation fairly simple so that the logic is easy to understand and test.

## What the project does

The program mainly handles these things:

* Loads delivery data from JSON files
* Assigns packages to available delivery agents
* Calculates the distance between locations
* Simulates the delivery process
* Calculates agent performance
* Finds the top-performing agent
* Generates JSON, CSV and text reports

## Project Structure

```text
FastBox_Delivery_System/
│
├── delivery_system.py
├── data.json
├── delivery_details.json
├── report.json
├── routes.txt
├── top_performer.csv
├── run_all_tests.py
├── README.md
├── REPORT.md
├── requirements.txt
│
└── test_cases/
    ├── test_case_1/
    ├── test_case_2/
    ├── ...
    └── test_case_10/
```

## Requirements

Python 3.9 or above should work.

The project mainly uses Python's standard libraries, so there are no complicated dependencies to install.

You can check your Python version with:

```bash
python --version
```

## How to Run

First, open the project folder in VS Code or a terminal.

Run the main program:

```bash
python delivery_system.py
```

The program will process the data and create/update the output files.

## Running the Test Cases

There are 10 test cases included with the project.

To run all of them:

```bash
python run_all_tests.py
```

This is useful for checking the program with different input situations instead of testing only one dataset.

## Input Data

The main input is stored in:

```text
data.json
```

The file contains information related to:

* Delivery agents
* Warehouses
* Packages
* Locations

You can change the data in this file and run the program again to test different cases.

## Output Files

After running the program, some of the generated files are:

### `report.json`

Contains the delivery and agent performance summary.

### `delivery_details.json`

Contains details about individual package deliveries.

### `top_performer.csv`

Stores the information about the top-performing delivery agent.

### `routes.txt`

Contains the generated delivery route information in a simple text format.

## How the Assignment Works

The basic flow of the program is:

```text
Input Data
    ↓
Load JSON Data
    ↓
Assign Packages
    ↓
Calculate Delivery Distance
    ↓
Simulate Delivery
    ↓
Calculate Agent Performance
    ↓
Generate Reports
```

For package assignment, the program checks the available agents and uses their locations to decide which agent should handle the package.

After assignment, the delivery distance is calculated and the results are used to calculate the agent's performance.

## Custom Testing

If you want to test your own data, you can modify `data.json`.

For example, you can change:

* Number of packages
* Package destinations
* Warehouse locations
* Number of delivery agents
* Agent locations

After changing the data, run:

```bash
python delivery_system.py
```

You can then check the generated JSON, CSV and text files for the results.

## Notes

I tried to keep the code straightforward rather than adding unnecessary frameworks or libraries. The main focus of the project is the delivery assignment logic, distance calculation, simulation and report generation.

The test cases are also included in the repository so the implementation can be checked with the provided scenarios.
