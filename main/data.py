from google.cloud import bigquery
import pandas as pd

from utils.params import *

class DataLoader:

    def __init__(self, project_id:str, dataset_id:str, table_id:str):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id

    def load_data(self) -> pd.DataFrame:

            """
                Function to load data from bigquery to pandas dataframe
            """

            client = bigquery.Client()
            query = f"""
            SELECT
                name,
                genres,
                popularity,
            FROM
                `{self.project_id}.{self.dataset_id}.{self.table_id}`
            """

            return client.query(query).to_dataframe()

if __name__ == "__main__":

    df = DataLoader(PROJECT_ID, DATASET_ID, TABLE_ID).load_data()

    print(df.shape)
    print(df.head())
