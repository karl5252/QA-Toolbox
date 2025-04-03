PATTERN = r'\d{2}\d{2}\d{4}\d{2}\d{2}\d{2}$'
EXCL_LIST = ['PROJECT ONE', 'PROJECT TWO']

TIMEOUT = 30
BASIC_URL = "https://example.atlassian.net/wiki/rest/api/"
GROUPS = ['productowner, scrummaster, stakeholder, teammember']
SPACE_LIMIT = 300
PER_PAGE = 25

URLS = {
    "list": lambda pages: f"space?start={pages}",
    "space": lambda key, group: f"/group/by-name?name={key} {group}",
    "delete_space": lambda key: f"space/{key}",
}
