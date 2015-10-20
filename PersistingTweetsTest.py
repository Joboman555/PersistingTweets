import unittest
import json
import PersistingTweets
import os

__author__ = 'jspear'


class TestPersistingTweets(unittest.TestCase):

    def test_getConsumerKey(self):
        data = {"ConsumerKey": "comsumerKeyTest",
                "ConsumerSecret": "consumerSecretTest"}

        with open('test.txt', 'w') as outfile:
            json.dump(data, outfile)

        consumerKey = PersistingTweets.getConsumerKey()
        self.assertEqual(consumerKey, "consumerKeyTest")

        os.remove('test.txt')
