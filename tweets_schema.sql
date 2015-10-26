-- Schema for Persisting Tweets application

-- Database representation of one tweet
create table tweets (
    id                  integer primary key,
    created_at          date,
    retweet_count       integer,
    tweet_text          text,
    user_screen_name    text,
    user_id             integer,
    user_utc_offset     integer,
    user_friends_count  integer,
    user_statuses_count integer
);
