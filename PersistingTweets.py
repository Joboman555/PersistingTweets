import time
import json
import Credentials
import tweepy
import collections
import sqlite3


def flatten(dictionary, parent_key='', seperator='_'):
    items = []
    for key, value, in dictionary.items():
        new_key = parent_key + seperator + key if parent_key else key
        if isinstance(value, collections.MutableMapping):
            items.extend(flatten(value, new_key, seperator).items())
        else:
            items.append((new_key, value))
    return dict(items)


def create_schema(schema_filename, conn):
    with open(schema_filename, 'rt') as schema_file:
        schema = schema_file.read()
        conn.executescript(schema)


def does_table_exist(tbl_name, conn):
    sql_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(tbl_name)
    table_exists = conn.execute(sql_query).fetchone()
    return table_exists


def store_tweet(db_filename, tweet_data):
    schema_filename = 'tweets_schema.sql'

    with sqlite3.connect(db_filename) as conn:
        if not does_table_exist('tweets', conn):
            print('Building database ...')
            create_schema(schema_filename, conn)
            print('Database built successfully...')
        conn.execute("INSERT INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(tweet_data))


def extract_tweet_data(data):
    keys = ['id', 'created_at', 'retweet_count', 'text', 'user_screen_name', 'user_id', 'user_utc_offset', 'user_friends_count', 'user_statuses_count']
    tweet_data = [data.get(key, None) for key in keys]
    return tweet_data


def print_db_values(db_filename, table_name):
    sql_query = 'SELECT * FROM {}'.format(table_name)
    with sqlite3.connect(db_filename) as conn:
        for row in conn.execute(sql_query):
            print row


class SQLDurationStreamListener(tweepy.StreamListener):

    # Gets a duration in seconds for which to stream tweets
    def __init__(self, streaming_duration, output_location):
        self.start_time = time.time()
        self.duration = streaming_duration
        self.output_location = output_location
        self.tweetsStored = 0

    def on_data(self, json_string):
        data = json.loads(json_string)
        # Tweets contain nested dictionary which needs to be flattened before storing
        data = flatten(data)
        # Extracts a few interesting keys so we can store them
        tweet_data = extract_tweet_data(data)
        store_tweet(self.output_location, tweet_data)

        # Show how many tweets have been stored
        self.tweetsStored += 1
        print('Tweets stored: ' + str(self.tweetsStored))

        # Check if time limit has been surpassed
        current_time = time.time()
        has_duration_ended = (current_time - self.start_time) > self.duration
        # Returning false will stop collection of tweets
        return not has_duration_ended

    def on_error(self, status_code):
        print status_code
        return False

if __name__ == '__main__':

    credentials_Location = "TwitterAPICredentials.json"

    auth = Credentials.getAuthentication(credentials_Location)

    output_location = 'tweets.db'
    streaming_duration = input('How many seconds would you like to collect Tweets for? ')
    myStreamListener = SQLDurationStreamListener(streaming_duration, output_location.strip())
    myStream = tweepy.Stream(auth, myStreamListener)
    try:
        myStream.filter(track=['python'])
    except KeyboardInterrupt:
        pass
    print_db_values(output_location, 'tweets')
