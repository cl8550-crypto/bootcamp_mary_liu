import pandas as pd

def fill_missing_age(df: pd.DataFrame) -> pd.DataFrame:
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())
    return df

def encode_sex(df: pd.DataFrame) -> pd.DataFrame:
    if "Sex" in df.columns:
        df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = fill_missing_age(df)
    df = encode_sex(df)
    return df
