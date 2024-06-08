from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rate', 'views')
    list_filter = ('user', 'categories')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'rate', 'views', 'isbn')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('categories',),
        }),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
