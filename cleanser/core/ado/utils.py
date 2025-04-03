from unittest.mock import MagicMock


def get_mocked_response():
    mock_data = {
        "value": [
            {
                "name": "DryRunProject-A",
                "id": "proj123",
                "lastUpdateTime": "2022-01-01T10:00:00.000Z"
            },
            {
                "name": "DryRunProject-B",
                "id": "proj456",
                "lastUpdateTime": "2021-10-01T15:30:00.000Z"
            }
        ]
    }

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data
    return mock_response
