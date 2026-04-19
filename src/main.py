import pandas as pd
import os

def load_full_grouped():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", "full_grouped.csv")

    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        print("full_grouped.csv loaded successfully")
        return df
    except Exception as e:
        print("Error:", e)
        return None


def load_country_wise_latest():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", "country_wise_latest.csv")

    try:
        df = pd.read_csv(file_path)
        print("country_wise_latest.csv loaded successfully")
        return df
    except Exception as e:
        print("Error:", e)
        return None

def explore_data(df, name):
    print(f"\n=== {name} OVERVIEW ===")
    
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nColumns:")
    print(df.columns)

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

def main():
    full_df = load_full_grouped()
    latest_df = load_country_wise_latest()

    if full_df is not None:
        explore_data(full_df, "FULL GROUPED DATA")

    if latest_df is not None:
        explore_data(latest_df, "COUNTRY LATEST DATA")


if __name__ == "__main__":
    main()

