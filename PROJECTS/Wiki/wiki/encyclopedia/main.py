# local lib
from . import util


def return_list_entries() -> list:
    list_entries = util.list_entries()
    return list_entries


# Save and convert to html file if article title not in list entries
# If check_exist_handline return None this function will return False 
# It mean what title not correct
def save_and_convert_file(content: str) -> tuple[str | None, bool]:
    list_entries = return_list_entries()
    title = return_modifided_title(content)
    check_correct_title = False

    if title is not None:
        # check exist of article
        if title in list_entries:
            title = None
            check_correct_title = True
        else:
            util.save_file(title, content, "md", util.ENTRIES_MD_DIR)
            util.convert_from_md_to_html(title)
            check_correct_title = True

    return title, check_correct_title
            

# Get content and return title or None if title not exist
def return_modifided_title(content: str) -> str | None:
    if not check_exist_handline(content):
        # in future will be popup window
        print("[!] No article name")
        return None
    else:
        try:
            # get headline and title
            headline = content.split("\n")[0].strip()
            title = headline[2:]

            # change title
            title = title.lower()
            title = title[0].upper() + title[1:]

            # return title
            return title
        except Exception as ex:
            print("[!] Some error") 
            print(ex) 
            return None


# True or False
def check_exist_handline(content: str) -> bool:
    if content[0] != "#":
        return False
    else:
        return True
