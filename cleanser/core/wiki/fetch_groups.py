from cleanser.const.confluence import BASIC_URL, URLS, GROUPS


def fetch_groups(session, space_key, dry_run=False):
    """
    Fetch all groups associated with the space
    {{protocol}}://{{host}}/wiki/rest/api/group/by-name?name={{group_name}}
    :param dry_run:
    :param session:
    :param space_key:
    :return:
    """
    if dry_run:
        print("Dry run. Returning empty json so projects are eligible for deletion")
        return []
    # GROUPS = ['productowner, scrummaster, stakeholder, teammember']
    for group in GROUPS:
        groups_list_url = f"{BASIC_URL}{URLS['space'](space_key, group)}"  # f'{basic_url}group/by-name?name={space_key} {group}'
        response = session.get(groups_list_url)
        return response
