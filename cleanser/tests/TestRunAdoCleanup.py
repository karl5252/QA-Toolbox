import unittest
from unittest.mock import patch, MagicMock

from cleanser.const.exit_codes import EXIT_CODES
from cleanser.core.ado.run_ado_cleanup import run_cleanup


class TestRunCleanup(unittest.TestCase):

    @patch('cleanser.core.ado.run_ado_cleanup.fetch_projects')
    @patch('cleanser.core.ado.run_ado_cleanup.requests.Session')
    def test_run_cleanup_dry_run(self, mock_session, mock_fetch_projects):
        mock_session.return_value = MagicMock()
        mock_fetch_projects.return_value.status_code = 200
        mock_fetch_projects.return_value.json.return_value = {"value": []}

        run_cleanup('fake_token', org='fake_org', dry_run=True)
        mock_fetch_projects.assert_called_once()

    @patch('cleanser.core.ado.run_ado_cleanup.fetch_projects')
    @patch('cleanser.core.ado.run_ado_cleanup.requests.Session')
    def test_run_cleanup_real_run(self, mock_session, mock_fetch_projects):
        mock_session.return_value = MagicMock()
        mock_fetch_projects.return_value.status_code = 200
        mock_fetch_projects.return_value.json.return_value = {"value": []}

        run_cleanup('fake_token', org='fake_org', dry_run=False)
        mock_fetch_projects.assert_called_once()

    @patch('cleanser.core.ado.run_ado_cleanup.fetch_projects')
    @patch('cleanser.core.ado.run_ado_cleanup.requests.Session')
    def test_run_cleanup_exit_on_error(self, mock_session, mock_fetch_projects):
        mock_session.return_value = MagicMock()
        mock_fetch_projects.return_value.status_code = 500

        with self.assertRaises(SystemExit):
            run_cleanup('fake_token', org='fake_org', dry_run=False)

    @patch('cleanser.core.ado.run_ado_cleanup.fetch_projects')
    @patch('cleanser.core.ado.run_ado_cleanup.requests.Session')
    def test_run_cleanup_exit_on_error(self, mock_session, mock_fetch_projects):
        mock_session.return_value = MagicMock()
        error_codes = {
            202: 0,
            200: 0,
            401: 10,
            403: 10,
            404: 20,
            429: 30,
            409: 40,
            500: 1  # Adding a default unexpected error for completeness
        }

        for status_code, expected_exit_code in error_codes.items():
            with self.subTest(status_code=status_code):
                mock_fetch_projects.return_value.status_code = status_code

                status, should_exit, _ = EXIT_CODES[expected_exit_code]
                if should_exit:
                    with self.assertRaises(SystemExit) as cm:
                        run_cleanup('fake_token', org='fake_org', dry_run=False)
                    self.assertEqual(cm.exception.code, expected_exit_code)
                else:
                    run_cleanup('fake_token', org='fake_org', dry_run=False)


if __name__ == '__main__':
    unittest.main()
