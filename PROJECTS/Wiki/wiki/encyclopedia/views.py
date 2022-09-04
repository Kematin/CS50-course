from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist

from . import util
list_entries = util.list_entries()


def index(request):
    # util.convert_and_save_html('Mirimo')
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries
    })

def open_article_page(request, article):
    try:
        for i in range(len(list_entries)):
            if article.lower() in list_entries[i].lower():
                return render(request, f"entries_html/{list_entries[i]}.html")
        else:
            return render(request, f"error/article_not_found.html")
                
    except TemplateDoesNotExist:
        print(f"[!] Article {article} not found")
        return render(request, f"error/article_not_found.html")

