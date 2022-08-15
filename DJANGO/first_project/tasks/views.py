from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'number': '1'
    })


def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
            return HttpResponseRedirect(reverse('tasks:index'))

        else:
            return render(request, 'tasks/add.html', {
                'form': form
            })

    return render(request, 'tasks/add.html', {
        'form': NewTaskForm(),
    })


class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')
