#!/usr/bin/python3
'''
    Python script that takes 2 arguments in order to solve this challenge
    the challenge is to get the first 10 commits
'''

import sys
import requests


if __name__ == "__main__":
    url = 'http://api.github.com/repos'
    repo = sys.argv[1]
    owner = sys.argv[2]
    request = '{}/{}/{}/commits'. format(url, owner, repo)
    commits = requests.get(request)
    commits = commits.json()
    for commit in commits[:10]:
        print('{}: {}'.
              format(commit.get('sha'),
                     commit.get('commit').get('author').get('name')))
