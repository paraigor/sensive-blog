from django.contrib import admin

from blog.models import Comment, Post, Tag, User


class TagInline(admin.TabularInline):
    model = Post.tags.through
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ["author", "likes",]
    exclude = ["tags"]
    inlines = [TagInline]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "post",]
    raw_id_fields = ["author",]


admin.site.register(Tag)
