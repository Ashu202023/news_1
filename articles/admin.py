from django.contrib import admin
from .models import Article 

class Aadmin(admin.ModelAdmin):
    list_display=(
        "title",
        "body",
        "author",
        "date",
    )


admin.site.register(Article,Aadmin)


# Register your models here.
