from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=200,
            height=200,
        )
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    inlines = [PlaceImageInline]
