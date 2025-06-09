from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)
    # list_display = __all__
    search_fields = ('title', 'price',)
    # readonly_fields = ('published_date',)

admin.site.register(Book, BookAdmin)