"""
This function is tailored for synchronizing with a GitHub repository and adding
problems to the database. You can execute this function directly from the 
terminal using the following command:

python challenges/manage.py sync_problems
"""
from django.core.management.base import BaseCommand
from challenges_app.models import Challenges
from django.db.utils import IntegrityError
import requests
import re

"""
Configuration data
"""
# Files which should not be imported into the database:
EXCEPTIONS = ["README.md", ".gitignore", "LICENSE", "tests"]
OWNER = "alum-challenges"
REPO_NAME = "problems"
BRANCH_NAME = "python/2022"
BASE_URL = "https://api.github.com/repos"

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Entry point for the management command
        self.sync_problems(OWNER, REPO_NAME, BRANCH_NAME)

    def sync_problems(self, owner, repo_name, branch_name):
        """
        Synchronize problems from a GitHub repository.

        :param owner: GitHub repository owner
        :param repo_name: GitHub repository name
        :param branch_name: Branch of the repository to sync
        """
        def explore_directory(directory_url):
            """
            Recursively explore the directory structure of the GitHub repository.

            :param directory_url: URL of the directory to explore
            """
            files = requests.get(directory_url).json()

            for file in files:
                if file["name"] not in EXCEPTIONS:
                    if file["type"] == "dir":
                        # Recursively explore subdirectories
                        explore_directory(file["url"])
                    elif file["name"].endswith(".md"):
                        # Process Markdown files
                        problem_url = file["download_url"]
                        response = requests.get(problem_url)

                        if response.status_code == 200:
                            # Save the Markdown content as a Challenge in the database
                            problem = response.text
                            try:
                                Challenges(title=file["name"].replace(".md", ""), description=problem).save()
                            except IntegrityError:
                                # Handle IntegrityError (e.g., duplicate entry) by ignoring it
                                pass

        # Start exploring the directory structure from the root of the specified branch
        branch_url = f"{BASE_URL}/{owner}/{repo_name}/contents?ref={branch_name}"
        explore_directory(branch_url)
