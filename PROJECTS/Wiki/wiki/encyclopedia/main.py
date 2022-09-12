# local lib
from . import util


def return_list_entries() -> list:
    list_entries = util.list_entries()
    return list_entries


# Return title or None if error
def save_file(content: str) -> str | None:
    if not check_exist_handline(content):
        # in future will be popup window
        print("[!] No article name")
    else:
        try:
            headline = content.split("\n")[0].strip()
            title = headline[2:]
            util.save_file(title, content, "md", util.ENTRIES_MD_DIR)
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
