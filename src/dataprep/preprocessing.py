from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

def create_preprocessor(df):
    """
    Defines categorical and numeric columns.
    Returns a ColumnTransformer for preprocessing.
    """

    categorical_cols = df.select_dtypes(include=["object", "bool"]).columns.tolist()
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", StandardScaler(), numeric_cols)
        ]
    )
    return preprocessor