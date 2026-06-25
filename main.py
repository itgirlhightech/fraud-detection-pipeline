from src.extract import extract
from src.transform import transform
from src.load import load


print("Iniciando extração...")
df = extract()


print("Iniciando transformação...")
df = transform(df)


print("Iniciando carregamento...")
load(df)


print("Pipeline concluído!")