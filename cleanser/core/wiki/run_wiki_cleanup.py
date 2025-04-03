from unittest.mock import MagicMock

import requests

from cleanser.core.wiki.fetch_spaces import fetch_spaces
from cleanser.core.wiki.wiki_cleanup import wiki_cleanup


def run_wiki_cleanup(username, password, dry_run=False):
    if dry_run:
        session = MagicMock()
        session.status_code = 200
        print(f"[DRY-RUN] Using mocked session. No requests will be sent.")
    else:
        session = requests.Session()
        session.auth = (username, password)
        session.headers.update({"Content-Type": "application/json"})
        session.headers.update({"Authorization": f"Basic {session.auth}"})

    spaces = fetch_spaces(session, dry_run)
    if spaces:
        # Extract only the required elements
        filtered_spaces = [
            {
                'id': space['id'],
                'key': space['key'],
                'name': space['name'],
                'status': space['status']
            }
            for space in spaces
        ]
        wiki_cleanup(session, filtered_spaces, dry_run)
    else:
        print("No spaces found or unable to fetch spaces.")
