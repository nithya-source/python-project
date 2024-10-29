from django.contrib import admin
from .models import LCategory,LPost,aboutusdb

# Register your models here.
class LPostAdmin (admin.ModelAdmin):
    list_display=('d_title','d_content')
    search_fields=('d_title','d_content')
    list_filter=('d_created_at','d_category_id')

admin.site.register(LPost,LPostAdmin)
admin.site.register(LCategory)
admin.site.register(aboutusdb)