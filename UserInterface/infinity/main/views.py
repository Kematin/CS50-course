from django.http import JsonResponse
from django.shortcuts import render

import time

# Create your views here.
def index(request):
    return render(request, "index.html")

def posts(request):
    # Get start point and end point
    start = int(request.GET.get("start") or 1)
    end = int(request.GET.get("end") or (start+9))

    # Get array of posts
    data = [f"Post #{i}" for i in range(start, end+1)]
    time.sleep(1)

    '''
    route ./posts?start=5 will return:
    {
        Posts: [
                "Post 5",
                "Post 6",
                ...,
                "Post 15"
            ]
    }
    route ./posts?start=5&end=6 will return: 
        {Posts: ["Post 5", "Post 6"]}
    '''
    return JsonResponse({
        "posts": data
    })
