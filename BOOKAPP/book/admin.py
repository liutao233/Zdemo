from django.contrib import admin
from .models import HeroInfo, BookInfo

# Register your models here.

# class HeroInfoInline(admin.StackedInline):
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ['btitle', 'bpub_date', 'bcomment', 'bread', 'my_date']
    search_fields = ['btitle']

    ###########编辑设置##########
    fieldsets = (
        ('必填', {'fields': ['btitle', 'bpub_date']}),
        ('选填', {'fields': ['bcomment', 'bread', 'is_delete'], 'classes': ['collapse',]})
    )

    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_per_page = 4
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ['hbook', 'hgender']
    list_display = ['hname', 'hcomment', 'hbook', 'hgender', 'book_read']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

admin.site.site_header = '疯狂书城'
admin.site.site_title = '疯狂书城MSI'
admin.site.index_title = '书城MSI'