import sqlite3
import pandas as pd
import datetime as dt

con = sqlite3.connect('C:/Users/pillai_amal/NSE_AMAL/DataBase_From_Jan/nsedb.db') #sqlfile
cur = con.cursor()

def make_time_series(ticker, days): #this function accepts the ticker and the days, days are counted reversely
    df = pd.read_sql(f"SELECT * FROM '{ticker}'", con)
    df.drop_duplicates(inplace= True)
    df.dropna()
    df['date']= pd.to_datetime(df['date']).dt.date
    df.set_index('date', inplace= True)
    df.sort_index(inplace= True)
    return(df.iloc[-days:])


# sample = make_time_series('AMIORG',29)
# print(sample)