from django.urls import path

from webapp.views.articles import add_view, detail_view, edit_task
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view),
    path('task/add/', add_view),
    path('task/', detail_view),
    path('task/edit/?pk=', edit_task),
]
