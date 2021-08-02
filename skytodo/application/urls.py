from django.conf.urls import handler404
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('task/dashboard', dashboard, name='dashboard'),
    path('task/create', task_create, name='task-create'),
    path('task/filter', task_filter, name='tag-filter'),
    path('task/filter/clear', task_filter_clear, name='tag-filter-clear'),
    path('task/<int:pk>/update', task_update, name='task-update'),
    path('task/<int:pk>/delete', task_delete, name='task-delete'),
    path('tag/create', tag_create, name='tag-create'),
    path('tag/<int:pk>/update', tag_update, name='tag-update'),
    path('tag/<int:pk>/delete', tag_delete, name='tag-delete'),
    path('tag/select', tag_select, name='tag-select-clear'),
    path('tag/select/<int:pk>', tag_select, name='tag-select'),
    path('task/dashboard/important/<int:level>', select_important, name='select-important'),
]

handler404 = page_not_found
