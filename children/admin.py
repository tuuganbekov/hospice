from django.contrib import admin

from children.models import Children, Application


@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "gift", "gift_price", )
    search_fields = ("full_name", )


@admin.register(Application)
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "time_to_call", "child", )
    search_fields = ("name", )
