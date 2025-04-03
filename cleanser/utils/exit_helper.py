import sys

from cleanser.const.exit_codes import EXIT_CODES


def exit_with(code: int):
    status, should_exit, message = EXIT_CODES.get(code, ("Unknown", True, "Unrecognized exit code"))
    print(f"[EXIT {code}] {status}: {message}")
    sys.exit(code if should_exit else 0)
