import unittest
from unittest.mock import patch, MagicMock

from cleanser.core.jira.run_jira_cleanup import run_jira_cleanup


class TestRunJiraCleanup(unittest.TestCase):

    @patch("cleanser.core.jira.run_jira_cleanup.fetch_projects")
    @patch("cleanser.core.jira.run_jira_cleanup.requests.Session")
    def test_run_jira_dry_run(self, mock_session, mock_fetch):
        mock_session.return_value = MagicMock()
        mock_fetch.return_value = {"value": [{"id": "123", "name": "DRY", "key": "DRY1", "archived": True}]}
        run_jira_cleanup("fake_token", dry_run=True)

    @patch("cleanser.core.jira.run_jira_cleanup.fetch_projects")
    @patch("cleanser.core.jira.run_jira_cleanup.requests.Session")
    def test_jira_cleanup_429(self, mock_session, mock_fetch):
        mock_session.return_value = MagicMock()
        response = MagicMock()
        response.status_code = 429
        mock_fetch.return_value = response
        with self.assertRaises(SystemExit) as cm:
            run_jira_cleanup("fake_token", dry_run=False)
        self.assertEqual(cm.exception.code, 30)


if __name__ == '__main__':
    unittest.main()
