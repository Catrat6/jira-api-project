import os
import json
import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('jira_email')
key = os.getenv('jira_key')

while True:
    issue = input('What is the issue ID?\n')

    url = f'https://isi-technology.atlassian.net/rest/api/2/issue/{issue}'

    auth = HTTPBasicAuth(username, key)

    headers = {
        'Accept': 'application/json'
    }

    query = {
        'jql': 'project = iSi Technology'
    }

    call = requests.request(
        'GET',
        url,
        headers=headers,
        params=query,
        auth=auth
    )

    call.raise_for_status()
    x = call.json()

    pprint.pp(x)
