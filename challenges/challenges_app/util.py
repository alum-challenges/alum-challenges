# Source: https://cs50.harvard.edu/web/2020/projects/1/wiki/
import re

from challenges_app.models import Challenges
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all markdown files, without the extension name
    """
    return Challenges.objects.values_list("title", flat=True)


def get_entry(title):
    """
    Retrieves a problem from database by its title. If no such
    file exists, the function returns None.
    """
    try:
        problem = Challenges.objects.get(title=title)
        return problem.description
    except Challenges.DoesNotExist:
        return None


def get_challenge(title):
    """
    Retrieves a problem from database by its title. If no such
    file exists, the function returns None.
    """
    try:
        return Challenges.objects.get(title=title)
    except Challenges.DoesNotExist:
        return None


def save_entry(title, content):
    """
    Saves a file, given its title and Markdown
    content. If an existing file with the same title already exists,
    it is replaced.
    """
    filename = f"problems/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
