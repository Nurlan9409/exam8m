from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Billing,Post
# Register your models here.


@admin.register(Billing)
class BillingAdmin(ImportExportModelAdmin):
    list_display = ('id', 'payment_type',  'created_date')
    list_display_links = ('id', 'payment_type', 'created_date')
    search_fields = ('id', 'payment_type',)
    list_filter = ('id', 'payment_type',)
    ordering = ('created_date',)

    def comments_text(self, obj):
        return obj.comments[:10]

"""@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'author' 'created_at')
    list_display_links = ('id', 'title', 'author' 'created_at')
    search_fields = ('id', 'title', 'author')
    list_filter = ('id', 'title', 'author')
    ordering = ('created_at',)
    def blogs_text(self, obj):
        return obj.blogs[:100]
"""