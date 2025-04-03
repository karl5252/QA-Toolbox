import requests

from cleanser.const.jira import BASIC_URL, EXCL_LIST, URLS, TIMEOUT


def fetch_projects(session, dry_run=False):
    """
    Return all spaces that match a specific pattern indicating those are automation leftovers. Spaces that are not
    matching or are part of exclusion groups should not be returned.
    Example of spaces that match:

    copying Electronics Sudanese Pound 25092024114133,
    mobile Fantastic deposit Beauty - Tools 20092024120624

    :return: List of filtered projects
    """
    automation_projects = []

    projects_list_url = f'{BASIC_URL}{URLS["projects"]}'
    if dry_run:
        return [
            {
                "id": "proj-123",
                "key": "DRY1",
                "name": "DryRunProject Alpha",
                "archived": True
            },
            {
                "id": "proj-456",
                "key": "DRY2",
                "name": "DryRunProject Beta",
                "archived": True
            }
        ]
    response = session.get(projects_list_url)
    if response.status_code == 200:
        projects = response.json()  # The response is a list of projects
        # List of project names to exclude

        for prj in projects:
            # get project etails using additonal detail enpint
            # {{protocol}}://{{host}}/{{basePath}}rest/api/3/project/{key}
            project_detail_url = f'{BASIC_URL}project/{prj["key"]}'
            try:
                project_detail_response = session.get(project_detail_url, timeout=TIMEOUT)
                if project_detail_response.status_code == 200:
                    project_detail = project_detail_response.json()
                    if project_detail.get('name') not in EXCL_LIST and project_detail.get(
                            'archived'):
                        filtered_project = {
                            'id': prj['id'],
                            'key': prj['key'],
                            'name': prj['name'],
                            'archived': prj['archived']
                        }
                        automation_projects.append(filtered_project)
                    else:
                        print(f"Project {prj['name']} is not archived or is in the exclusion list.")

            except requests.exceptions.RequestException as e:
                print(f"Failed to get project details for {prj['name']}. Refer to the error message: {e}")
    return automation_projects
