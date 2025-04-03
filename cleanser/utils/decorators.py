from functools import wraps

import requests

from cleanser.const.exit_codes import EXIT_CODES
from cleanser.utils.exit_helper import exit_with
from cleanser.utils.get_exit_code import get_exit_code_from_status


def handle_api_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            if hasattr(response, "status_code"):
                code = get_exit_code_from_status(response.status_code)
                status, should_exit, message = EXIT_CODES[code]
                print(f"[ACTION][{status}] {message}")
                if should_exit:
                    exit_with(code)
            return response

        except requests.exceptions.Timeout:
            print("[TIMEOUT] API call timed out.")
            exit_with(29)
        except requests.exceptions.ConnectionError:
            print("[CONNECTION ERROR] Could not reach the API.")
            exit_with(1)
        except requests.exceptions.RequestException as e:
            print(f"[REQUEST EXCEPTION] Unexpected error: {e}")
            exit_with(1)

    return wrapper
