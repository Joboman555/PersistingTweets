import time
import Credentials
import tweepy


class DurationStreamListener(tweepy.StreamListener):

    # Gets a duration in seconds for which to stream tweets
    def __init__(self, streaming_duration):
        self.start_time = time.time()
        self.duration = streaming_duration

    def on_data(self, data):
        print data.encode('utf-8')

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

    streaming_duration = input('How many seconds would you like to collect Tweets for? ')
    myStreamListener = DurationStreamListener(streaming_duration)
    myStream = tweepy.Stream(auth, myStreamListener)
    try:
        myStream.filter(track=['python'])
    except KeyboardInterrupt:
        pass
