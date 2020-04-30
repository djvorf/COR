from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Lector, Reviews, LectorImages


@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ("numberPart", "name", "url", "draft")
    list_display_links = ("name", "numberPart", "url")
    list_filter = ("name", "numberPart")
    search_fields = ("name", "numberPart")
    save_on_top = True
    list_editable = ("draft", )
    fieldsets = (
        (None, {
            "fields": (("numberPart", "name", "url", "draft"), )
        }),
        (None, {
            "fields": ("shortInfo", "content")
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name")
    list_display_links = ("name", "email", "id")
    list_filter = ("name", "email")
    search_fields = ("name", "email")
    save_on_top = True


@admin.register(LectorImages)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image", "lector", "get_image")
    list_display_links = ("title", "description", "image", "lector", "get_image")
    list_filter = ("title", "description", "image", "lector")
    search_fields = ("title", "description", "image", "lector")
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width="60" height="60"')

    get_image.short_description = "Изображение"
