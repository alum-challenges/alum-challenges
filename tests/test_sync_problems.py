from unittest.mock import patch, call
from django.test import TestCase, TransactionTestCase
from challenges_app.models import Challenges
from challenges_app.management.commands.sync_problems import Command


class TestSyncProblems(TransactionTestCase):

    # mock glob variable, so sync_problems function grabs files from other directory
    @patch("challenges_app.management.commands.sync_problems.subprocess.run")
    @patch("challenges_app.management.commands.sync_problems.glob")
    def test_sync_problems(self, mock_glob, mock_subprocess_run):

        mock_subprocess_run.return_value.returncode = 0
        mock_glob.return_value = [
            "tests/tests_files/rectangle.md",
        ]

        command = Command()
        command.sync_problems()

        expected_calls = [
            call(
                ["git", "pull"],
                cwd="tests/tests_files/rectangle.md",
            )
        ]

        mock_subprocess_run.assert_has_calls(expected_calls, any_order=True)

        # assert data in database
        self.assertEqual(Challenges.objects.count(), 1)

        self.assertIsNotNone(Challenges.objects.get(title="rectangle"))

        self.assertEqual(Challenges.objects.get(title="rectangle").author, "Dana-f559")
        self.assertEqual(
            Challenges.objects.get(title="rectangle").full_title,
            "Perimeter of a Rectangle",
        )
        self.assertEqual(
            Challenges.objects.get(
                week="0", course="CS50P", topics='["Functions", "Variables"]'
            ).title,
            "rectangle",
        )
