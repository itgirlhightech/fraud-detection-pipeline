import pandas as pd


def transform(df):
    df.fillna(0, inplace=True)
    df = df.rename(columns={'Class': 'suspeita'})
    df['suspeita'] = df['suspeita'] == 1
    df['valor_alto'] = df['Amount'] > 1000
    total = df['suspeita'].sum()
    print(f"Total de transações suspeitas: {total}")
    return df

if __name__ == "__main__":
    from extract import extract
    df = extract()
    transform(df)