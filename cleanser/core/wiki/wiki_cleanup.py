
from cleanser.const.confluence import URLS, BASIC_URL, TIMEOUT
from cleanser.const.exit_codes import EXIT_CODES
from cleanser.core.wiki.fetch_groups import fetch_groups
from cleanser.core.wiki.utils import filter_spaces
from cleanser.utils.decorators import handle_api_errors
from cleanser.utils.get_exit_code import get_exit_code_from_status


@handle_api_errors
def wiki_cleanup(session, automation_spaces, dry_run=False):
    print("Space key recycler starting...")
    if automation_spaces:
        filtered_spaces = filter_spaces(automation_spaces)
        for count, project in enumerate(filtered_spaces, 1):
            print(project["name"], project["key"])
            if fetch_groups(session, project['key'], dry_run):
                print(f"Group exists for space {project['name']}")
                return
            else:
                if dry_run:
                    print("Dry run mode. THose spaces would have been deleted:")
                    print(f"##[command]Deleting space {project['name']}")
                    print(f"##[command]Deleting space {project['key']}")
                else:
                    print(f"Group does not exist for space {project['name']} can safely delete space")
                    print("deleting space")
                    key = project['key']
                    delete_url = f"{BASIC_URL}{URLS['delete_url'](key)}"

                    delete_response = session.delete(delete_url, timeout=TIMEOUT)
                    exit_code = get_exit_code_from_status(delete_response.status_code)
                    status, should_exit, message = EXIT_CODES[exit_code]
                    print(f"[ACTION][{status}] {message} while deleting {project['name']}")
