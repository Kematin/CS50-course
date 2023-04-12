from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NewTaskForm as task_form

# Create your views here.
def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []

    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasks'],
        'number': '1'
    })


def add(request):
    if request.method == 'POST':
        form = task_form(request.POST)

        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse('tasks:index'))

        else:
            return render(request, 'tasks/add.html', {
                'form': form
            })

    return render(request, 'tasks/add.html', {
        'form': task_form(),
    })

