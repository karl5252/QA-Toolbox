from cleanser.const.confluence import EXCL_LIST, SPACE_LIMIT, BASIC_URL, URLS, PER_PAGE


def fetch_spaces(session, dry_run=False):
    """
    return all spaces that match specific pattern indicating those are automation leftovers. Spaces that are not
     matching or are part of exclusion groups should be not returned.
    Example of spaces that match:

    copying Electronics Sudanese Pound 25092024114133,
    mobile Fantastic deposit Beauty - Tools 20092024120624

    :return:
    """
    if dry_run:
        print("Dry run mode fetching dummy spaces...")
        return [
            {
                "id": 197003787,
                "key": "DHHIOOAERT",
                "name": " ARCHIVED deposit Human Hills interfaces 11112024063553",
                "status": "archived"
            },
            {
                "id": 191857770,
                "key": "DIWVZ",
                "name": " ARCHIVED deposit incremental Wells value-added 06112024120849",
                "status": "archived"
            },
            {
                "id": 176955085,
                "key": "DISGPO",
                "name": " ARCHIVED deposit Intelligent Soft Gloves Plain 14102024121050",
                "status": "archived"
            },
            {
                "id": 252480890,
                "key": "DLNS",
                "name": " ARCHIVED deposit Lempira navigate Spring",
                "status": "archived"
            },
            {
                "id": 252907511,
                "key": "DSAIA",
                "name": " ARCHIVED deposit Soft auxiliary Investment Account",
                "status": "archived"
            },
            {
                "id": 251428870,
                "key": "DSWC",
                "name": " ARCHIVED deposit Sweden withdrawal Corporate",
                "status": "archived"
            }
        ]

    automation_spaces = []
    max_spaces = 300  # to adjust based on the number of total spaces (safe range is around 300 pages)
    for i in range(0, SPACE_LIMIT, PER_PAGE):
        spaces_list_url_tmp = f"{BASIC_URL}{URLS['pages'](i)}"  # f'{spaces_list_url}{i}'
        response = session.get(spaces_list_url_tmp)
        if response.status_code == 200:
            spaces = response.json()['results']

            automation_spaces = automation_spaces + [
                space for space in spaces
                if space.get('status') == 'archived'
                   and space.get('name') not in EXCL_LIST
                   and 'ARCHIVED' in space.get('name')
                # and re.search(pattern, space.get('name'))  # leave this for now depedning on the automation approach
            ]
    return automation_spaces
