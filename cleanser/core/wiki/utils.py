def filter_spaces(automation_spaces):
    return [
        {
            'id': space['id'],
            'key': space['key'],
            'name': space['name'],
            'status': space['status']
        }
        for space in automation_spaces
    ]
