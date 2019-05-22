from django.contrib import admin

from .models import News,Category

class CategoryInline(admin.TabularInline):
    model = Category.news.through


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','is_published','date_published']

    inlines = [
        CategoryInline
    ]

admin.site.register(News,NewsAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    exclude = ['news']

admin.site.register(Category,CategoryAdmin)




#admin.site.register()