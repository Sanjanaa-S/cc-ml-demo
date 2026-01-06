import pandas as pd

def load_housing_data(path="data/housing_dataset.csv"):
    """
    Load the housing dataset CSV.
    """
    df = pd.read_csv(path)
    return df
