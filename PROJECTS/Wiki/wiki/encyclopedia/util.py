import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from markdown2 import Markdown

ENTRIES_MD_DIR = 'entries/'
ENTRIES_HTML_DIR = 'encyclopedia/templates/entries_html/'

def list_entries() -> list:
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_file(title: str, content: str, type: str, dir: str) -> None:
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"{dir}/{title}.{type}"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        print(f"[!] File {title}.{type} was already exist and was delete")

    default_storage.save(filename, ContentFile(content))
    print(f"[+] File {title}.{type} was write with new content")


def get_content_from_file(title: str, type: str, dir: str) -> str | None:
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"{dir}{title}.{type}")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def convert_from_md_and_save_html(title: str) -> None:
    # Convert from md to html
    markdowner = Markdown()
    md_content = get_content_from_file(title, 'md', ENTRIES_MD_DIR)
    if md_content is None:
        print(f"[!] File {title}.md not found")
    else:
        html_content = markdowner.convert(md_content)
        filename = ENTRIES_HTML_DIR + title
        
        # Check exist of file
        if default_storage.exists(filename):
            default_storage.delete(filename)
            print(f"[!] File {title}.html was already exist")

        # Save file with name title.html
        else:
            save_file(title, html_content, 'html', ENTRIES_HTML_DIR)
            print(f"[+] Convert {title}.md to {title}.html was complete")

            # Edit html file
            content = get_content_from_file(title, 'html', ENTRIES_HTML_DIR).split('\n')
            if content is None:
                print(f"[!] File {title}.html not found")
            else:
                edit_content_html(title, content)

def edit_content_html(title: str, content: list):
    print(f'[+] Start edit {title}.html')
    content = ['    ' + item for item in content]
    initial_content = [
                '{% extends "encyclopedia/layout.html" %}', 
                '{% block title %}',
                '   Article',
                '{% endblock %}',
                '{% block body %}'
               ]
    final_content = ['{% endblock %}']
    total_content = initial_content + content + final_content

    # Save html file with new content
    filename = f"{ENTRIES_HTML_DIR}/{title}.html"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        print(f"[!] File {title}.html was already exist and was delete")

    with open(filename, 'w', encoding='utf-8') as f:
        for string in total_content:
            f.write(string)
        print(f"[+] File {title}.html was write with new content")


