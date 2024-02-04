# Pagination
from django.core.paginator import Paginator


def is_htmx(request, boost_check=True):
    """
    Check if request comes from htmx
    """
    hx_boost = request.headers.get("Hx-Boosted")
    print(f"hx_boost: {hx_boost}")
    hx_request = request.headers.get("Hx-Request")
    print(f"hx_request: {hx_request}")
    if boost_check and not hx_boost:
        return False
    elif boost_check and hx_boost and hx_request:
        return True


def paginate(request, qs, limit=2):
    """
    Paginate QuerySet(qs)
    Return
    """
    paginated_qs = Paginator(qs, limit)
    print(f"Num_pages: {paginated_qs.num_pages}")
    page_no = request.GET.get("page")
    print(f"Page_no: {page_no}")
    return paginated_qs.get_page(page_no)


# Source: https://cs50.harvard.edu/web/2020/projects/1/wiki/
import re

from challenges_app.models import Challenges
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import frontmatter


def list_entries():
    """
    Returns a list of all markdown files, without the extension name
    """
    entries = list(Challenges.objects.order_by("course", "week"))

    # entries = list(map(add_metadata, entries))
    return entries


def add_metadata(challenge):
    """
    Adds metadata from the frontmatter to a Challenge object
    """
    challenge.meta = frontmatter.loads(challenge.description).__dict__
    return challenge


def get_entry(title):
    """
    Retrieves a problem from database by its title. If no such
    file exists, the function returns None.
    """
    try:
        problem = Challenges.objects.get(title=title)
        problem = re.sub(r"^---\n[\s\S]+?\n---\n", "", problem.description)
        return problem.strip()
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
