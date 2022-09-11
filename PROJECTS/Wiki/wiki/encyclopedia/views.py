from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse

from random import choice

from . import util
from .forms import TextareaForm

list_entries = util.list_entries()
def index(request):
    for item in list_entries:
        util.convert_from_md_to_html(item)
    random_page = choice(list_entries)
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries,
        "random_page": random_page,
    })


def open_article_page(request, article):
    try:
        random_page = choice(list_entries)
        for i in range(len(list_entries)):
            if article.lower() in list_entries[i].lower():
                return render(request, f"entries_html/{list_entries[i]}.html", {
                    "random_page": random_page,
                })
        else:
            print(f"[!] Article {article} not found")
            return render(request, f"error/article_not_found.html")
                
    except TemplateDoesNotExist:
        print(f"[!] Article {article} not found")
        return render(request, f"error/article_not_found.html")


def add_new_article(request):
    if request.method == 'POST':
        form = TextareaForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['textarea_form']
            save_file(content)
            return HttpResponseRedirect(reverse('add'))

    else:
        return render(request, "encyclopedia/add_page.html", 
                      {"textarea_form": TextareaForm()})


def handler404(request):
    return render(request, "error/404.html", {})


def save_file(content: str) -> None:
    if not check_exist_handline(content):
        # in future will be popup window
        print("[!] No article name")
    else:
        try:
            headline = content.split("\n")[0].strip()
            title = headline[2:]
            util.save_file(title, content, "md", util.ENTRIES_MD_DIR)
        except Exception as ex:
            print("[!] Some error") 
            print(ex) 


def check_exist_handline(content: str) -> bool:
    if content[0] != "#":
        return False
    else:
        return True
