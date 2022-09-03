import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from markdown2 import Markdown

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        print(f"[!] File {title}.md was already exist and was delete")

    default_storage.save(filename, ContentFile(content))
    print(f"[+] File {title}.md was write with new content")


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def convert_and_save_html(title):
    # Convert from md to html
    markdowner = Markdown()
    md_content = get_entry(title)
    if md_content is None:
        print(f"[!] File {title}.md not found")
    else:
        html_content = markdowner.convert(md_content)

        # Save file with name title.html
        filename = f"encyclopedia/templates/entries_html/{title}.html"
        if default_storage.exists(filename):
            default_storage.delete(filename)
            print(f"[!] File {title}.html was already exist and was delete")

        default_storage.save(filename, ContentFile(html_content))
        print(f"[+] Convert {title}.md to {title}.html was complete")
