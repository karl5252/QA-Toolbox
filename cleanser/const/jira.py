PATTERN = r'\d{2}\d{2}\d{4}\d{2}\d{2}\d{2}$'
EXCL_LIST = ['PROJECT ONE', 'PROJECT TWO']

# time
TIMEOUT = 30
MAX_RETRIES = 5
MIN_WAIT = 5
MAX_WAIT = 15

BASIC_URL = "https://example.atlassian.net/rest/api/3/"
URLS = {
    "projects": "project",
    "unarchive": lambda key: f"project/{key}/restore",
    "delete": lambda key: f"project/{key}",
}
