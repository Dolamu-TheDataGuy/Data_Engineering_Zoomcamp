import os
import pandas as pd
from time import time
from sqlalchemy import create_engine
import pyarrow as pa
from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    database = os.getenv('POSTGRES_DB')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    url = os.getenv('URL')
    table_name = os.getenv('TABLE_NAME')
    
    # connect to database
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    conn = engine.connect()
    
    source_file = 'data.parquet'
    
    os.system(f"wget {url} -O {source_file}")
    
    pd.read_parquet("data.parquet").to_csv("data.csv") #convert parquet to csv
    
    df_iter = pd.read_csv("data.csv", iterator=True, chunksize=100000) # convert to a generator
    
    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df.drop("Unnamed: 0", axis=1, inplace=True)
            df.to_sql(name="yellow_taxi_data", con=conn, if_exists='append')
            t_end = time()
            print(f"Inserted another chunk, took {t_end-t_start:3f} seconds")
        except StopIteration:
            print("Finished ingesting all dataset to dataset")
            break
    
    
    


if __name__ == "__main__":
    main()