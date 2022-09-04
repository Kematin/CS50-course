from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist

from random import choice

from . import util


list_entries = util.list_entries()
def index(request):
    # for item in list_entries:
    #     util.convert_and_save_html(item)
    random_page = choice(list_entries)
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries,
        "random_page": random_page,
    })

def open_article_page(request, article):
    try:
        for i in range(len(list_entries)):
            if article.lower() in list_entries[i].lower():
                return render(request, f"entries_html/{list_entries[i]}.html")
        else:
            print(f"[!] Article {article} not found")
            return render(request, f"error/article_not_found.html")
                
    except TemplateDoesNotExist:
        print(f"[!] Article {article} not found")
        return render(request, f"error/article_not_found.html")

def add_new_article(request):
    return render(request, "encyclopedia/add_page.html")

