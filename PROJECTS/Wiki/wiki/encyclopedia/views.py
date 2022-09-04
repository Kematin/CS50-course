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
    if article in list_entries:
        try:
            return render(request, f"entries_html/{article}.html")
        except TemplateDoesNotExist:
            print(f"[!] Article {article} not found")
            return render(request, f"error/article_not_found.html")

    else:
        print(f"[!] Article {article} not found")
        return render(request, f"error/article_not_found.html")
