from django.contrib import admin
from .models import Advertise, PromotionChannel


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    """Настройки админки для рекламных кампаний."""
    list_display: tuple = ('id', 'name', 'product', 'budget')
    list_display_links: tuple = ('id', 'name')
    search_fields: tuple = ('name',)
    list_editable: tuple = ('budget',)
    list_select_related: bool = True
    autocomplete_fields: tuple = ("product",)


@admin.register(PromotionChannel)
class PromotionAdmin(admin.ModelAdmin):
    """
    Настройки для добавления и отображения каналов
    продвижения рекламных кампаний.
    """
    list_display = ('id', 'name')
    list_display_links: tuple = ('id', 'name')
