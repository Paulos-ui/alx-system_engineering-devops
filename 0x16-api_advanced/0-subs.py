#!/usr/bin/python3
"""Function to query subscribers on a given Reddit sub reddit."""

from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """ This returns the number subscribers,
       returns 0 if the request is invalid
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user = {'User-agent': 'Paulos-ui'}
    response = get(url, headers=user)
    resp = response.json()

    try:
        return resp.get('data').get('subscribers')
    except Exception:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
