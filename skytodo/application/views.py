from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *

def index(request):
    data = {}
    data['form'] = ContactForm
    return render(request, "public/index.html", data)

@login_required
def dashboard(request):
    data = {}
    data['tags'] = request.user.tag_list.all()
    data['tag'] = None
    data['time'] = request.session.get('time', 0)
    data['important'] = request.session.get('important', 0)
    data['tag_id'] = request.session.get('tag_id', None)
    data['status'] = request.session.get('status', 'all')
    data['time_priority'] = request.session.get('time_priority', 'all')
    data['important_priority'] = request.session.get('important_priority', 'all')
    data['formfilter'] = TaskFilterForm(initial=data)
    data['tag'] = request.user.tag_list.filter(pk=data['tag_id']).first()
    criteria = {}
    if data['tag']: criteria['tags'] = data['tag']
    if data['status'] != 'all': criteria['status'] = data['status']
    if data['time_priority'] != 'all': criteria['time_priority'] = data['time_priority']
    if data['important_priority'] != 'all': criteria['important_priority'] = data['important_priority']
    data['items'] = request.user.task_list.filter(**criteria).all()
    return render(request, "task/dashboard.html", data)

@login_required
def task_create(request):
    data = {}
    data['tags'] = request.user.tag_list.all()
    initial = {}
    initial['user']= request.user
    initial['status'] = 'to-do'
    initial['time_priority'] = '0'
    initial['subject_priority'] = '0'
    if request.method == "POST":
        data['form'] = TaskForm(request.POST, initial=initial)
        if data['form'].is_valid():
            instance = data['form'].save()
            instance.user = request.user
            instance.save()
            return redirect('dashboard')
        else:
            pass
    else:
        data['form'] = TaskForm(initial=initial)
    return render(request, "task/create.html", data)

@login_required
def task_update(request, pk):
    data = {}
    data['tags'] = request.user.tag_list.all()
    try:
        data['instance'] = Task.objects.get(pk=pk)
    except:
        pass
    if request.method == "POST":
        data['form'] = TaskForm(request.POST, instance=data['instance'])
        if data['form'].is_valid():
            instance = data['form'].save()
            return redirect('dashboard')
        else:
            pass
    else:
        data['form'] = TaskForm(instance=data['instance'])
    return render(request, "task/update.html", data)

@login_required
def task_delete(request, pk):
    data = {}
    data['tags'] = request.user.tag_list.all()
    try:
        data['instance'] = Task.objects.get(pk=pk)
    except:
        pass
    if request.method == "POST":
        data['instance'].delete()
        return redirect('dashboard')
    else:
        data['form'] = TaskForm(instance=data['instance'])
    data['form'].readonly()
    return render(request, "task/delete.html", data)

@login_required
def tag_create(request):
    data = {}
    data['tags'] = request.user.tag_list.all()
    initial = {}
    if request.method == "POST":
        data['form'] = TagForm(request.POST, initial=initial)
        if data['form'].is_valid():
            instance = data['form'].save()
            instance.user = request.user
            instance.save()
            return redirect('dashboard')
        else:
            pass
    else:
        data['form'] = TagForm(initial=initial)
    return render(request, "tag/create.html", data)

@login_required
def tag_update(request, pk):
    data = {}
    data['tags'] = request.user.tag_list.all()
    try:
        data['instance'] = Tag.objects.get(pk=pk)
    except:
        pass
    if request.method == "POST":
        data['form'] = TagForm(request.POST, instance=data['instance'])
        if data['form'].is_valid():
            instance = data['form'].save()
            return redirect('dashboard')
        else:
            pass
    else:
        data['form'] = TagForm(instance=data['instance'])
    return render(request, "tag/update.html", data)

@login_required
def tag_delete(request, pk):
    data = {}
    data['tags'] = request.user.tag_list.all()
    try:
        data['instance'] = Tag.objects.get(pk=pk)
    except:
        pass
    if request.method == "POST":
        data['instance'].delete()
        return redirect('dashboard')
    else:
        data['form'] = TagForm(instance=data['instance'])
    data['form'].readonly()
    return render(request, "tag/delete.html", data)

@login_required
def task_filter(request):
    data = {}
    data['tags'] = request.user.tag_list.all()
    if request.method == "POST":
        form = TaskFilterForm(request.POST)
        if form.is_valid():
            for key in ['time_priority', 'important_priority', 'status']:
                request.session[key] = form.cleaned_data[key]
    return redirect('dashboard')

@login_required
def task_filter_clear(request):
    for key in ['time_priority', 'important_priority', 'status']:
        del request.session[key]
    return redirect('dashboard')

@login_required
def tag_select(request, pk=None):
    if pk:
        request.session['tag_id'] = pk
    else:
        request.session['tag_id'] = None
    return redirect('dashboard')

@login_required
def select_time(request, level):
    if -2 <= level <= 2:
        request.session['time'] = level
    return redirect('/task/dashboard')

@login_required
def logout(request):
    return redirect('/task/dashboard')

@login_required
def select_important(request, level):
    if -2 <= level <= 2:
        request.session['important'] = level
    return redirect('/task/dashboard')

def page_not_found(request):
    return redirect('/')
