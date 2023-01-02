from django.contrib import admin
from panel.models import Iteam
# Register your models here.
#admin.site.register(Iteam)

@admin.register(Iteam)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title',]
    prepopulated_fields = {'slug': ('title',)}