import pandas as pd
from src.transform import transform

def test_data():
    df = pd.DataFrame({'Amount': [150.0, 2000.0, 50.0, 5000.0, 800.0],
                     'Class': [0, 1, 0, 1, 0] })

    resultado = transform(df)

    assert 'suspeita' in resultado.columns
    assert resultado['Amount'].isnull().sum() == 0
    assert resultado.loc[resultado['Amount'] > 1000, 'valor_alto'].all() == True
    assert resultado.loc[resultado['suspeita'] == True, 'suspeita'].all() == True