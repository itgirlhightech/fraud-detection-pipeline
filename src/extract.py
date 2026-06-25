import pandas as pd

def extract():
    df = pd.read_csv('data/creditcard.csv')
    print(df.head())
    return df



if __name__ == "__main__":
    extract()