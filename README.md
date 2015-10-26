# PersistingTweets
This project's goal was to stream twitter data and store it in an sqlite database. Using it, you can specify keywords to search for
and a time limit to collect tweets.
### Running My Code

Before using Persisting Tweets, create a json file titled TwitterAPICredentials.json with the following format:

    {
        "ConsumerKey": "YOUR CONSUMER KEY HERE",
        "ConsumerSecret": "YOUR CONSUMER SECRET HERE",
        "AccessToken": "YOUR ACCESS TOKEN HERE",
        "AccessTokenSecret": "YOUR ACCESS TOKEN SECRET HERE"
    }
    
(If you don't have the required credentials you can request them from [Twitter](https://dev.twitter.com/oauth/overview/application-owner-access-tokens).)

##### After writing your credentials file:

1. Run PersistingTweets.py
2. Input the time period you'd like to stream tweets for
2. Input any keywords that you'd like to search new tweets for

Persisting Tweets will then get all new tweets that contain *any* of those given keywords, 
and store them in a local sqlite database file titled 'tweets.db'. After the time period is up, all of the stored tweets
are then displayed.

### Things I Learned in the Process:

The biggest skill I gained by doing this project was an increasing familiarity with python, the language itself. Having come
from a background working in much more rigorous languages, such as Java, C# and Haskell, python's loose and flexible style
seemed problematic for when writing projects more than a few lines of codes. Doing this small project showed me how powerful
of a tool python can be in the area of rapid prototyping and development, and made me feel confident in choosing python for 
medium to large projects in the future. Along the way, I had to do a learn a lot of other stuff indluding:

* Writing database schema
* Locally storing data via python's [sqlite3](https://docs.python.org/2/library/sqlite3.html) library
* Accessing twitter's streaming API using [tweepy](https://github.com/tweepy/tweepy)
* Converting to and from json and python
* Python project organization
* Making markup files (how'd I do?)

### Cool Room for Expansion

Now that I've gotten the basic twitter streaming and persistent storage mechanism down, there are a lot of cool things that can be done.
Some of these ideas include:

* Gauging public perception of companies from collected twitter data using [indico's sentiment analysis](https://docs.indico.io/v1.0/docs/sentiment)
to predict rises and falls in the stock market. 
* Looking at which words make a tweet get more retweets.
* Using tweets' geographical location tag to gain insight on regional dialects throughout the united states.
* Comparing popularity of programming languages by directly comparing amount of mentions on twitter.
