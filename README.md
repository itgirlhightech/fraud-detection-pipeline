# Fraud Detection Pipeline

## Overview

This project is a simple Fraud Detection Data Pipeline built to demonstrate fundamental concepts of Data Engineering, including ETL processes, SQL analysis, automated testing, and Continuous Integration (CI).

The pipeline extracts transaction data, transforms and validates the information, loads it into a SQLite database, and provides SQL queries for analysis.

## Objectives

* Build a simple ETL pipeline using Python.
* Practice data extraction, transformation, and loading processes.
* Perform fraud-related data analysis using SQL.
* Implement automated testing with Pytest.
* Apply Continuous Integration (CI) using GitHub Actions.
* Develop a project structure similar to real-world Data Engineering workflows.

## Project Structure

```text
fraud-detection-pipeline/
│
├── .github/workflows/
│   └── ci.yml
│
├── data/
│
├── sql/
│   └── analysis.sql
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── __init__.py
│
├── tests/
│   └── test_transform.py
│
├── main.py
├── requirements.txt
└── README.md
```

## ETL Process

### Extract

Reads transaction data from a CSV dataset.

### Transform

* Handles missing values.
* Identifies suspicious transactions.
* Creates a high-value transaction flag.
* Applies basic fraud detection rules.

### Load

Stores the processed data into a SQLite database for analysis.

## SQL Analysis

The project includes SQL queries for:

* Fraud transaction analysis.
* High-value transaction identification.
* Data exploration and reporting.

## Automated Testing

Unit tests were implemented using Pytest to validate:

* Missing value handling.
* Fraud flag creation.
* High-value transaction classification.
* Data transformation logic.

Run tests with:

```bash
python -m pytest
```

## Continuous Integration

GitHub Actions automatically:

* Sets up the Python environment.
* Installs project dependencies.
* Runs automated tests on every push and pull request.

## Technologies Used

* Python
* Pandas
* SQLite
* SQL
* Pytest
* Git
* GitHub
* GitHub Actions

## Data Source

This project uses the [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) 
dataset from Kaggle, provided by the Machine Learning Group of ULB (Université Libre de Bruxelles).

The dataset contains 284,807 transactions, of which 492 are fraudulent.

