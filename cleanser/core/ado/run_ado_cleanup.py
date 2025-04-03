import base64

import requests

from cleanser.const.ado import ORGANIZATIONS
from cleanser.const.exit_codes import EXIT_CODES
from cleanser.core.ado.ado_cleanup import ado_cleanup
from cleanser.core.ado.fetch_projects import fetch_projects
from cleanser.utils.exit_helper import exit_with
from cleanser.utils.get_exit_code import get_exit_code_from_status


def run_cleanup(token, org=None, dry_run=False):
    orgs = [org] if org else ORGANIZATIONS

    for org in orgs:
        base_url = f"https://dev.azure.com/{org}"
        session = requests.Session()

        if dry_run:
            print(f"[DRY-RUN] Using mocked session. No requests will be sent.")
        else:
            auth = str(base64.b64encode(f":{token}".encode()), "ascii")
            session.headers.update({"Authorization": f"Basic {auth}"})

        # ↓ fetch_projects always returns a Response-like object
        response = fetch_projects(session, base_url, dry_run)

        code = get_exit_code_from_status(response.status_code)
        status, should_exit, message = EXIT_CODES[code]
        print(f"[{status}] {message} while fetching projects from {org}")
        if should_exit:
            exit_with(code)

        projects = response.json()
        ado_cleanup(session, base_url, projects, dry_run)
