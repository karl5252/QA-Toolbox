import re
from datetime import datetime, timedelta

from cleanser.const.ado import PATTERN, DATE_CUTOFF, EXCL_LIST, URLS, TIMEOUT
from cleanser.const.exit_codes import EXIT_CODES
from cleanser.utils.decorators import handle_api_errors
from cleanser.utils.get_exit_code import get_exit_code_from_status


@handle_api_errors
def ado_cleanup(session, base_url, projects, dry_run=False):
    # print(projects)
    now = datetime.now()
    cutoff = now - timedelta(days=DATE_CUTOFF)

    for project in projects['value']:
        try:
            project_created_date = datetime.strptime(project['lastUpdateTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            project_created_date = datetime.strptime(project['lastUpdateTime'], '%Y-%m-%dT%H:%M:%SZ')

        # Check if the project is older than a year
        if project_created_date < cutoff or re.search(PATTERN, project.get('name')):
            if project['name'] in EXCL_LIST:
                continue
            print(f"Deleting project {project['name']} with ID {project['id']}")
            project_id = project['id']
            delete_endpoint = URLS["delete_project"](project_id)
            delete_url = f"{base_url}{delete_endpoint}"  # to consider urlib.parse in the future

            # Check if dry-run is enabled
            if dry_run:
                print(f"[DRY-RUN] Would delete project {project['name']} with ID {project['id']}")
                continue

            delete_response = session.delete(delete_url, timeout=TIMEOUT)
            exit_code = get_exit_code_from_status(delete_response.status_code)
            status, should_exit, message = EXIT_CODES[exit_code]
            print(f"[ACTION][{status}] {message} while deleting {project['name']}")
