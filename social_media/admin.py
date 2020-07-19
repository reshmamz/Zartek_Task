from django.contrib import admin
from social_media.models import Feed, Image, Tag, Like

# Register your models here.

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1



admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Like)



@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    '''Admin View for Feed'''

    list_display = ('name', 'description')
    filter_horizontal = ('tag',)
    inlines = [
        ImageInline,
    ]