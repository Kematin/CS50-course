# local lib
from . import util

# ----------------- MAIN -----------------


# Save and convert to html file if article title not in list entries
# If check_exist_handline return None this function will return False 
# It mean what title not correct
def save_new_file_and_convert_to_html(content: str) -> tuple[str | None, bool]:
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
            util.edit_content_and_save_file(title)
            check_correct_title = True

    return title, check_correct_title
            

# If check_exist_handline return None this function will return None
# It mean what title not correct
def edit_file_and_convert_to_html(content: str) -> str | None:
    title = return_modifided_title(content)

    if title is not None:
        util.save_file(title, content, "md", util.ENTRIES_MD_DIR)
        util.edit_content_and_edit_file(title)

    return title



# ----------------- UTILITY -----------------



# Return title or None if title not exist
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
            title = change_title(title)

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


def return_list_entries() -> list:
    list_entries = util.list_entries()
    return list_entries


def change_title(title: str) -> str:
    title = title.lower()
    title = title[0].upper() + title[1:]
    return title
