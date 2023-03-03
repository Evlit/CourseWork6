from django.contrib import admin

from ads.models import Ad, Comment

admin.site.register(Comment)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("title",)
