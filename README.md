# House Price Prediction

## Overview
This repository contains a machine learning project for predicting house prices based on various features. It includes full data preprocessing, exploratory data analysis (EDA), and multiple regression models including **Linear Regression, Ridge Regression, Random Forest, and XGBoost Regressor**. Each model is implemented as a modular Python package and can be trained independently.  

The project is organized for reproducible ML experiments, with dedicated directories for data, notebooks, and source code.

---

## Dataset
The dataset is included in this repository (`data/housing_dataset.csv`) and contains information about houses in a residential area. The dataset has the following columns:

| Column               | Description                            |
|---------------------|----------------------------------------|
| price               | Price of the house                      |
| area                | Area of the house                       |
| bedrooms            | Number of bedrooms                      |
| bathrooms           | Number of bathrooms                     |
| stories             | Number of stories                       |
| mainroad            | Whether the house is connected to a main road (yes/no) |
| guestroom           | Whether the house has a guest room (yes/no) |
| basement            | Whether the house has a basement (yes/no) |
| hotwaterheating     | Whether the house has hotwater heating (yes/no) |
| airconditioning     | Whether the house has air conditioning (yes/no) |
| parking             | Number of parking spaces                |
| prefarea            | Whether the house is in a preferred area (yes/no) |
| furnishingstatus    | Furnishing status of the house (unfurnished/semi-furnished/furnished) |

---

## Setup

### 1. Clone the Repository

```bash
git clone <repo-url>
cd cc-ml-demo
```

### 2. Create and Activate a Python Virtual Environment

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Upgrade pip (optional but recommended)

```bash
pip install --upgrade pip
```

### 4. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Dataset Location

Ensure that the dataset file is in the correct folder:

```
data/housing_dataset.csv
```

### 6. Running Model Training Scripts

You can train each model independently using the following commands:

```bash
python -m src.linear.train   # Train Linear Regression
python -m src.ridge.train    # Train Ridge Regression
python -m src.rf.train       # Train Random Forest Regressor
python -m src.xgb.train      # Train XGBoost Regressor
```

### 7. Launch Jupyter Notebooks

For exploration, EDA, and experimenting with models:

```bash
jupyter notebook notebooks/
```

---