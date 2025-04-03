import base64
from unittest.mock import MagicMock

import requests

from cleanser.core.jira.fetch_projects import fetch_projects
from cleanser.core.jira.jira_cleanup import jira_cleanup
from cleanser.core.jira.jira_restore import jira_restore


def run_jira_cleanup(token, dry_run=False):
    if dry_run:
        session = MagicMock()
        session.status_code = 200
        print(f"[DRY-RUN] Using mocked session. No requests will be sent.")
    else:
        session = requests.Session()
        auth = str(base64.b64encode(f":{token}".encode()), "ascii")
        session.headers.update({"Authorization": f"Basic {auth}"})

    projects = fetch_projects(session, dry_run)
    # print(projects)
    jira_restore(session, projects, dry_run)
    jira_cleanup(session, projects, dry_run)
