from django.contrib import admin
from .models import Article,Comment

# class Commentline(admin.StackedInline):
class Commentline(admin.TabularInline):

    model=Comment 
    extra=1
    # fields=(
    #     "author",
    #     "comment",
    # )


class Aadmin(admin.ModelAdmin):
    inlines=[Commentline,]
    list_display=(
        "title",
        "body",
        "author",
        "date",
    )


admin.site.register(Article,Aadmin)
admin.site.register(Comment)


# Register your models here.
