import pandas as pd

def load_sample_data():
    df = pd.read_csv("data/sample.csv")
    print("Loaded data:")
    print(df)
    return df

if __name__ == "__main__":
    load_sample_data()
