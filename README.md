# Finding Underrated People on Twitter with TURI (Twitter Underrated Index)

This repository holds scripts used to make calls to the Twitter API (via
the [python-twitter](https://github.com/bear/python-twitter) package to
calculate user's TURI (Twitter Underrated Index): an index that attempts to
figure out who is underrated on Twitter and therefore a good candidate to
follow.

[This corresponding blog post](http://www.marknagelberg.com/how-to-find-underrated-people-on-twitter-with-turi-twitter-underrated-index) goes into more detail about the reasoning
behind the index and how it works.

To run the code, you have to add a file to the main directory called
api_credentials.py. Within this file, you need to add the following dict:

```python
credentials = {'consumer_key':'insert_your_consumer_key',
               'consumer_secret':'insert_your_consumer_secret',
               'access_token_key':'insert_your_access_token_key',
               'access_token_secret':'insert your access token secret',
               'sleep_on_rate_limit':True}
```
