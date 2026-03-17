# Sea Level Predictor

This project analyzes historical global sea level data and predicts future sea level rise using linear regression techniques.

The dataset contains measurements from **1880 to 2014**, and the goal is to estimate how sea levels may change by the year **2050**.

---

## Project Objective

The main objective is to:

* Visualize historical sea level data
* Identify long-term trends
* Predict future sea level rise using statistical methods

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* SciPy

---

## Dataset

The dataset used:

```
epa-sea-level.csv
```

### Columns:

* **Year** → Year of observation
* **CSIRO Adjusted Sea Level** → Sea level change (in inches)

---

## What This Project Does

### 1. Scatter Plot

A scatter plot is created using:

* X-axis → Year
* Y-axis → Sea Level (inches)

This shows how sea level has changed over time.

---

### 2. First Line of Best Fit (All Data)

A regression line is calculated using the entire dataset (1880–2014).

* Represents the **overall long-term trend**
* Extended to the year **2050** for prediction

---

### 3. Second Line of Best Fit (From 2000)

A second regression line is calculated using data from the year **2000 onwards**.

* Represents the **recent trend**
* Helps identify if sea level rise is accelerating

---

## Final Output

The final graph includes:

* Scatter plot of historical data
* Red line → Prediction using all data
* Green line → Prediction using recent data

---

## Project Structure

```
├── epa-sea-level.csv
├── sea_level_predictor.py
├── main.py
├── test_module.py
└── README.md
```

---

## How to Run

### 1. Install dependencies

```
pip install pandas matplotlib scipy
```

### 2. Run the project

```
python main.py
```

---

## Learning Outcomes

This project demonstrates:

* Data visualization using scatter plots
* Linear regression for prediction
* Trend analysis using real-world data
* Working with time-series datasets

---

## About

This project is part of the **freeCodeCamp Data Analysis with Python Certification**.

It reflects practical skills used in real-world data analysis and forecasting problems.
