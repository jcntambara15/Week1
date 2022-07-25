import requests
import pprint
import pandas as pd
import sqlalchemy as db
from googleapiclient.discovery import build


def get_response(username):
    """Defining a function to retrieve data from my google API"""
    try:
        service_name = 'youtube'
        version = 'v3'
        Api_key = 'AIzaSyDtu3JOSDedjqU_avyy-GWtBY0IFUHXkT8'
        youtube_service = build(service_name, version, developerKey=Api_key)

        my_request = youtube_service.channels().list(
          part='statistics',
          forUsername=username)
        return my_request.execute()
    except ValueError:
        return "There is no channel associated to {username}!"

# username_example = FelixTechTips, schafer5, etc
def create_database(response):
    """Creating the dataframe and the database in general."""
    try:
        data = response['items'][0]['statistics']
        df = pd.DataFrame.from_dict(
          data,
          orient='index', 
          columns=['Channel'])
        engine = db.create_engine('sqlite:///my_youtube.db')
        df.to_sql('data', con=engine, if_exists='replace', index=True)
        return pd.DataFrame(engine.execute("SELECT * FROM data;").fetchall())
    except KeyError:
        return "There is no items key associated with your username!"


# Have a user input a username they want to get channel info for
your_username = input("Enter a username")
response = get_response(your_username)
pprint.pprint(response)
print(create_database(response))