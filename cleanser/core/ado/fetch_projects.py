import sys
from unittest.mock import MagicMock

import requests

from cleanser.const.ado import URLS, TIMEOUT


def fetch_projects(session: requests.Session, base_url: str, dry_run=False) -> requests.Response:
    url = f"{base_url}{URLS['projects']}"

    if dry_run:
        mock_response = MagicMock(spec=requests.Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "value": [
                {"name": "DryRunProject-A", "id": "proj123", "lastUpdateTime": "2022-01-01T10:00:00.000Z"},
                {"name": "DryRunProject-B", "id": "proj456", "lastUpdateTime": "2021-10-01T15:30:00.000Z"}
            ]
        }
        return mock_response

    try:
        return session.get(url, timeout=TIMEOUT)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch projects. Refer to the error message: {e}")
        sys.exit(1)
