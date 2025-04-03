EXIT_CODES = {
    0: ("OK", False, "Cleanup completed successfully"),
    1: ("Unexpected Error", True, "Unexpected error occurred"),
    2: ("Invalid Args", True, "Missing or invalid CLI arguments"),
    10: ("Auth Failed", True, "Authorization failed (401/403)"),
    20: ("Not Found", False, "API endpoint misconfigured or resource not found (404)"),
    29: ("Timeout", True, "No response from API or timeout occurred"),
    30: ("Throttled", True, "Rate limit reached (HTTP 429)"),
    40: ("Protected", False, "Protected resource detected, skipped (e.g. shared group)"),
    99: ("Dry Run", False, "Dry-run completed successfully"),
}
