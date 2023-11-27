import sqlite3
import pandas as pd

dataset = pd.read_csv(filepath_or_buffer='dataset_id-date-title-link.csv', names=['id', 'date', 'title', 'link'])
conn = sqlite3.connect('dataset.db')
dataset.to_sql(name='threads', con=conn, if_exists='replace')