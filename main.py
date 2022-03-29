import pandas as pd


def get_dataframe(json_path):
    return pd.read_json(json_path, lines=True)
