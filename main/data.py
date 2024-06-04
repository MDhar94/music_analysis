from google.cloud import bigquery
import pandas as pd

from utils.params import *

class DataLoader:

    def __init__(self):
        self.project_id = PROJECT_ID
        self.dataset_id = DATASET_ID
        self.table_id_artist = TABLE_ID_ARTIST
        self.table_id_tracks = TABLE_ID_TRACKS

    def load_data(self, is_artist=True) -> pd.DataFrame:

            """
                Function to load data from bigquery to pandas dataframe
            """

            client = bigquery.Client()

            if is_artist:
                query = f"""
                SELECT
                    name,
                    genres,
                    popularity,
                FROM
                    `{self.project_id}.{self.dataset_id}.{self.table_id_arist}`
                """

            else:
                query = f"""
                SELECT
                    *
                FROM
                    `{self.project_id}.{self.dataset_id}.{self.table_id_tracks}`
                """

            return client.query(query).to_dataframe()

if __name__ == "__main__":

    df = DataLoader(PROJECT_ID, DATASET_ID, TABLE_ID).load_data()

    print(df.shape)
    print(df.head())
