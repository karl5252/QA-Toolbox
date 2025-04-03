import requests

from cleanser.const.jira import BASIC_URL, URLS
from cleanser.core.jira.utils import safe_post


def jira_restore(session, projects, dry_run=False):
    """
    Restore the projects that were previously archived so could be deleted.
    :param session:
    :param projects:
    :param dry_run:
    :return:
    """
    for count, project in enumerate(projects, 1):
        print(project["name"], project["key"])
        print("un- archiving project")
        un_archive_url = f"{BASIC_URL}{URLS['unarchive'](project['key'])}"

        if dry_run:
            print(f"[DRY-RUN] Would unarchive project {project['name']} with ID {project['id']}")
            continue
        try:
            safe_post(session, un_archive_url)
        except requests.exceptions.RequestException as e:
            print(f"Failed to unarchive project {project['name']}. Refer to the error message: {e}")
            continue
