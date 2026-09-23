# FastBox Mystery Delivery System

A simple Python solution for the FastBox delivery-system assignment.

## What it does

1. Reads the JSON input file.
2. Finds the nearest agent for every package using Euclidean distance.
3. Calculates the delivery distance.
4. Creates `report.json` with package count, total distance, and efficiency.
5. Exports a small route summary and CSV file as bonus work.

## Run

```bash
python delivery_system.py
```

Run all supplied test cases:

```bash
python run_all_tests.py
```

No third-party Python packages are required.

## Distance rule

For every package the trip is calculated as:

`agent -> warehouse + warehouse -> destination`

The nearest agent is selected using the agent's starting location. Each package is treated as an individual trip because the assignment does not define a multi-stop route or route optimization rule.

## Project files

- `delivery_system.py` - main solution
- `data.json` - base input
- `report.json` - generated base report
- `delivery_details.json` - per-package distance details
- `routes.txt` - simple ASCII route summary
- `top_performer.csv` - bonus CSV export
- `run_all_tests.py` - runs the 10 supplied cases
- `test_cases/` - supplied input cases
- `test_reports/` - generated reports
- `REPORT.md` - assignment report
