from django.contrib import admin
from .models import Category, Pin, Board, SavedPin, SearchLog

admin.site.register(Category)
admin.site.register(Pin)
admin.site.register(Board)
admin.site.register(SavedPin)
admin.site.register(SearchLog)
