import pandas as pd

def iqr_outliers(df: pd.DataFrame, column: str, k: float = 1.5):
    """
    Flag outliers in a column using the IQR rule.
    Returns the DataFrame with a new boolean column: <col>_outlier
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - k*IQR, Q3 + k*IQR
    df[column + "_outlier"] = (df[column] < lower) | (df[column] > upper)
    return df
