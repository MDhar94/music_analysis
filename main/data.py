from google.cloud import bigquery
import pandas as pd

from utils.params import *

class DataLoader:

    def __init__(self):
        self.project_id = PROJECT_ID
        self.dataset_id = DATASET_ID
        self.table_id_artist = TABLE_ID_ARTISTS
        self.table_id_tracks = TABLE_ID_TRACKS

    def load_data(self, is_artist=True) -> pd.DataFrame:

            """
                Function to load data from bigquery to pandas

                'is_artist' = True for artists table, False for tracks table
            """

            client = bigquery.Client()

            if is_artist:
                query = f"""
                SELECT
                    id,
                    name,
                    genres,
                    popularity,
                FROM
                    `{self.project_id}.{self.dataset_id}.{self.table_id_artist}`
                """

            else:
                query = f"""
                SELECT
                    id,
                    id_artists,
                    popularity,
                    danceability,
                    energy,
                    loudness,
                    speechiness,
                    acousticness,
                    instrumentalness,
                    liveness,
                    valence,
                    tempo
                FROM
                    `{self.project_id}.{self.dataset_id}.{self.table_id_tracks}`
                """

            return client.query(query).to_dataframe()

    def load_data_subsample(self, is_artist=True, subsample=10) -> pd.DataFrame:

            """
                Function to load a random sample of data from bigquery to pandas dataframe

                'is_artist' = True for artists table, False for tracks table

                'subsample' = percentage of data to load
            """

            client = bigquery.Client()

            if is_artist:
                query = f"""
                SELECT
                    id,
                    name,
                    genres,
                    popularity,
                FROM
                    `{self.project_id}.{self.dataset_id}.{self.table_id_artist}`
                TABLESAMPLE SYSTEM ({subsample} PERCENT)
                """

            else:
                query = f"""
                SELECT
                    id,
                    id_artists,
                    popularity,
                    danceability,
                    energy,
                    loudness,
                    speechiness,
                    acousticness,
                    instrumentalness,
                    liveness,
                    valence,
                    tempo
                FROM
                    `{self.project_id}.{self.dataset_id}.{self.table_id_tracks}`
                TABLESAMPLE SYSTEM ({subsample} PERCENT)
                """

            return client.query(query).to_dataframe()

if __name__ == "__main__":

    # test to load data from artists table
    df = DataLoader(PROJECT_ID, DATASET_ID, TABLE_ID_ARTISTS).load_data()

    print(df.shape)
    print(df.head())
