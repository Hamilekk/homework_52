from django.contrib import admin

from webapp.models import ToDoList


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'due_date')
    list_filter = ('id', 'description', 'status', 'due_date')
    search_fields = ('description', 'status', 'id')
    fields = ('description', 'status', 'due_date')
    readonly_fields = ('id', 'due_date')


admin.site.register(ToDoList, ToDoAdmin)
