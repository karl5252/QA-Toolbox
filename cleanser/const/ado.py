PATTERN = r'\b\d{2}\d{2}\d{4}\d{2}\d{2}\d{2}\b.*$'
# exclusion list
EXCL_LIST = ['PROJECT ONE', 'PROJECT TWO']
# org list
ORGANIZATIONS = ["sample-org-1", "sample-org-2", "sample-org-3"]
# time
DATE_CUTOFF = 90
TIMEOUT = 30

# API version
API_VERSION = "7.1-preview.4"
# URLS
URLS = {
    "projects": f"/_apis/projects?api-version={API_VERSION}",
    "delete_project": lambda project_id: f"/_apis/projects/{project_id}?api-version={API_VERSION}",
    "users": f"/_apis/userentitlements?api-version=5.1-preview.2",
}
