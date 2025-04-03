from cleanser.const.exit_codes import EXIT_CODES
from cleanser.const.jira import EXCL_LIST, URLS, TIMEOUT, BASIC_URL
from cleanser.utils.decorators import handle_api_errors
from cleanser.utils.get_exit_code import get_exit_code_from_status


@handle_api_errors
def jira_cleanup(session, projects, dry_run=False):
    for project in projects:
        print(project)
        if project.get('name') not in EXCL_LIST and project.get('archived'):
            print(f"Deleting project {project['name']} with ID {project['id']}")
            delete_url = f"{BASIC_URL}{URLS['delete'](project['id'])}"

            # Check if dry-run is enabled
            if dry_run:
                print(f"[DRY-RUN] Would delete project {project['name']} with ID {project['id']}")
                continue

            # Make the API request to delete the project

            delete_response = session.delete(delete_url, timeout=TIMEOUT)
            exit_code = get_exit_code_from_status(delete_response.status_code)
            status, should_exit, message = EXIT_CODES[exit_code]
            print(f"[ACTION][{status}] {message} while deleting {project['name']}")
