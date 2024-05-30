from google.cloud import bigquery
import pandas as pd

from utils.params import *

def load_artist_data(project_id:str, dataset:str, table:str) -> pd.DataFrame:

    """Function to load data from bigquery to pandas dataframe"""

    # breakpoint()

    client = bigquery.Client()

    query = f"""
    SELECT
        name,
        genres,
        popularity,
    FROM
        `{project_id}.{dataset}.{table}`
    """

    df = client.query(query).to_dataframe()

    return df

if __name__ == "__main__":

    df = load_artist_data(PROJECT_ID, DATASET_ID, TABLE_ID)
    print(df.shape)
    print(df.head())
