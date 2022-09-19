import re

# django
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# theard party lib
from markdown2 import Markdown

# global verb, dir
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
    if check_exist_file(filename):
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


def check_exist_file(filename: str) -> bool:
    if default_storage.exists(filename):
        return True
    return False


def convert_from_md_to_html(title: str) -> None:
    # Convert from md to html
    markdowner = Markdown()
    md_content = get_content_from_file(title, 'md', ENTRIES_MD_DIR)
    if md_content is None:
        print(f"[!] File {title}.md not found")
    else:
        html_content = markdowner.convert(md_content).split('\n')
        edit_content_html(title, html_content)



def content_consolidation(content: list) -> list:
    content = ['    ' + item for item in content]
    initial_content = [
                '{% extends "encyclopedia/layout.html" %}', 
                '{% block title %}',
                '   Article',
                '{% endblock %}',
                '{% block body %}',
               ]
    final_content = [
            '   <form action="/edit/{{ title }}">',
                    '<p><input id="submit_edit_page" class="submit" type="submit"style="width: 80px; height:30px"value="Edit page"></p>',
            '   </form>',
            '{% endblock %}',
            ]
    total_content = initial_content + content + final_content
    return total_content


def edit_content_html(title: str, content: list) -> None:
    # Check exist file
    filename = f"{ENTRIES_HTML_DIR}/{title}.html"
    if check_exist_file(filename):
        print(f"[!] File {title}.html was already exist")

    # Save file with new content
    else:
        # Get content
        content = content_consolidation(content)

        # Write file with new content
        with open(filename, 'w', encoding='utf-8') as f:
            for string in content:
                f.write(string + '\n')
            print(f"[+] File {title}.html was write with new content")

