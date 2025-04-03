def get_exit_code_from_status(status_code: int) -> int:
    return {
        202: 0,
        200: 0,
        401: 10,
        403: 10,
        404: 20,
        429: 30,
        409: 40,
    }.get(status_code, 1)  # default: unexpected error
