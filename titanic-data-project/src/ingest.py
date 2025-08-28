import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
DATA_PATH = os.getenv("DATA_PATH", "data/raw/titanic.csv")

def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)

if __name__ == "__main__":
    df = load_data()
    print(df.head())
