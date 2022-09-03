from django.shortcuts import render

from . import util


def index(request):
    # util.convert_and_save_html('Django')
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

