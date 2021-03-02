import pandas as pd

file_name = "binary.csv"


def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()


print(retornaArq(file_name))
