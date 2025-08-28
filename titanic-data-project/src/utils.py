import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Lowercase and replace spaces with underscores in column names.
    Returns the same DataFrame object (in-place change).
    """
    df.columns = df.columns.str.lower().str.replace(" ", "_", regex=False)
    return df
