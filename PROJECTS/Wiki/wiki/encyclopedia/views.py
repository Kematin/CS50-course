# django
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist

# theard party lib
from random import choice

# local lib
from . import util
from .forms import TextareaForm
from .main import *

# -------------------------- MAIN ROUTES --------------------------



def index(request):
    list_entries = return_list_entries()
    for item in list_entries:
        util.convert_from_md_to_html(item)
    random_page = choice(list_entries)
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries,
        "random_page": random_page,
    })


def open_article_page(request, article: str):
    try:
        # get list entries and random page
        list_entries = return_list_entries()
        random_page = choice(list_entries)

        # check exist of article
        for i in range(len(list_entries)):
            if article.lower() in list_entries[i].lower():
                return render(request, f"entries_html/{list_entries[i]}.html", {
                    "random_page": random_page,
                    "title": list_entries[i]
                })
        else:
            print(f"[!] Article {article} not found")
            return render(request, f"error/article_not_found.html")
                
    except TemplateDoesNotExist:
        print(f"[!] Article {article} not found")
        return render(request, f"error/article_not_found.html")


def add_new_article(request):
    # get list entries and random page
    list_entries = return_list_entries()
    random_page = choice(list_entries)

    if request.method == 'POST':
        form = TextareaForm(request.POST)

        if form.is_valid():

            # get content from textarea and save to md
            content = form.cleaned_data['textarea_form']
            compose = save_and_convert_file(content)

            # compose = (title, check_correct_title)
            match compose:
                case (str(), True):
                    title = compose[0]
                    dir = f"entries_html/{title}.html"
                    return render(request, dir, {"random_page": random_page,})

                case (str() | None, False): return handler_uncorret_title(request)
                case (None, False | True): return handler_already_create_article(request)
                    
    else:
        return render(request, "encyclopedia/add_page.html", 
                      {"textarea_form": TextareaForm(),
                       "random_page": random_page})


def edit_article(request, title):
    content = util.get_content_from_file(title, "md", util.ENTRIES_MD_DIR)
    if content == None:
        return render(request, "error/article_not_found.html")

    title = title.lower()
    title = title[0].upper() + title[1:]
    context = {
            "title": title,
            "content": content,
        }

    if request.method == "POST":
        textarea_content = request.POST["textarea"]
        print(textarea_content)

    return render(request, "encyclopedia/edit_page.html", context)


# -------------------------- HANDLERS --------------------------



def handler404(request):
    return render(request, "error/404.html", {})


def handler_already_create_article(request):
    return render(request, "error/article_exist.html")


def handler_uncorret_title(request):
    return render(request, "error/title_uncorrect.html")
