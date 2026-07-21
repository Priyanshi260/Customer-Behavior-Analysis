# Data Cleaning with Python

## Overview

This project is part of an end-to-end data analytics workflow. The Python component is responsible for loading, cleaning, and preprocessing a raw dataset. The cleaned dataset is then prepared for further analysis in MySQL to generate business insights and for visualization in Power BI through interactive dashboards.

## Project Structure

```text
project/
│── main.py
│── README.md
│── requirements.txt
│── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│── src/
│   ├── load_data.py
│   └── clean_data.py
```

## Features

* Load raw data from a CSV file
* Handle missing values
* Remove duplicate records
* Standardize and clean the dataset
* Save the cleaned dataset for further analysis

## Technologies Used

### Python

* Python 3
* Pandas

### Upcoming Project Components

* MySQL (Business Insights)
* Power BI (Interactive Dashboards)

## Installation

1. Clone the repository:

```bash
git clone <https://github.com/Priyanshi260/Customer-Behavior-Analysis>
```

2. Navigate to the project directory:

```bash
cd <customer_shopping_behaviour_analysis>
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the project using:

```bash
python main.py
```

After execution, the cleaned dataset will be saved in the `data` folder.

## Project Files

* **main.py** – Executes the complete data cleaning pipeline.
* **src/load_data.py** – Contains functions for loading the dataset.
* **src/clean_data.py** – Contains functions for cleaning and preprocessing the dataset.
* **data/raw_data.csv** – Original dataset.
* **data/cleaned_data.csv** – Cleaned dataset generated after preprocessing.
* **requirements.txt** – Lists the required Python libraries.

## Output

The cleaned dataset is generated as:

```text
data/cleaned_data.csv
```

This cleaned dataset serves as the input for the next stages of the project:

* MySQL for business insights and analytical queries.
* Power BI for creating interactive dashboards and visualizations.

## Future Work

* Import the cleaned dataset into MySQL.
* Perform SQL queries to extract meaningful business insights.
* Build an interactive Power BI dashboard to visualize key metrics and trends.

## Author

**Priyanshi Jindal**
