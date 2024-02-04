from unittest.mock import patch, call
from django.test import TransactionTestCase
from challenges_app.models import Challenges
from challenges_app.management.commands.sync_problems import Command
import os


class TestSyncProblems(TransactionTestCase):

    def setUp(self):
        # Save the current working directory
        self.original_cwd = os.getcwd()

    def tearDown(self):
        # Restore the original working directory
        os.chdir(self.original_cwd)

    @patch("challenges_app.management.commands.sync_problems.subprocess.run")
    @patch("challenges_app.management.commands.sync_problems.glob")
    def test_sync_problems(self, mock_glob, mock_subprocess_run):
        mock_subprocess_run.return_value.returncode = 0

        # Mock glob to return the directory first and then the files
        mock_glob.side_effect = [["tests/tests_files"], ["rectangle.md"]]

        command = Command()
        command.sync_problems()

        expected_calls = [
            call(
                'git clone "git@github.com:alum-challenges/problems.git" "problems" 2> /dev/null || git -C "problems" pull',
                shell=True,
                cwd="tests/tests_files",
            ),
        ]
        mock_subprocess_run.assert_has_calls(expected_calls, any_order=True)

        # assert data in the database
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

    # Testing empty return value from glob function
    @patch("challenges_app.management.commands.sync_problems.subprocess.run")
    @patch("challenges_app.management.commands.sync_problems.glob")
    def test_empty_glob(self, mock_glob, mock_subprocess_run):
        mock_glob.return_value = []

        command = Command()
        command.sync_problems()

        self.assertEqual(Challenges.objects.count(), 0)

    # Testing adding duplicate file to the database
    @patch("challenges_app.management.commands.sync_problems.subprocess.run")
    @patch("challenges_app.management.commands.sync_problems.glob")
    def test_duplicate_file(self, mock_glob, mock_subprocess_run):
        mock_subprocess_run.return_value.returncode = 0

        # Mock glob to return the directory first and then the files
        mock_glob.side_effect = [["tests/tests_files"], [], [], ["rectangle.md"]]

        command = Command()
        command.sync_problems()
        # Call function twice with the same file
        command.sync_problems()

        self.assertEqual(Challenges.objects.count(), 1)

    # Testing updating data if adding a problem with the same title
    @patch("challenges_app.management.commands.sync_problems.subprocess.run")
    @patch("challenges_app.management.commands.sync_problems.glob")
    def test_updating_data(self, mock_glob, mock_subprocess_run):
        mock_subprocess_run.return_value.returncode = 0

        # Mock glob to return the directory first and then the files
        mock_glob.side_effect = [["tests/tests_files"], ["rectangle.md"]]

        Challenges.objects.create(
            title="rectangle",
            full_title="Test problem",
            description="duplicate",
            course="CS50P",
            week="0",
            author="None",
        )

        command = Command()
        command.sync_problems()

        self.assertEqual(Challenges.objects.get(title="rectangle").title, "rectangle")
        self.assertEqual(
            Challenges.objects.get(title="rectangle").full_title,
            "Perimeter of a Rectangle",
        )
        self.assertEqual(Challenges.objects.get(title="rectangle").author, "Dana-f559")
        self.assertEqual(Challenges.objects.count(), 1)
