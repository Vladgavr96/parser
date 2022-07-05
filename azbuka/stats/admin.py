from django.contrib import admin
from .models import Couch


@admin.register(Couch)
class CouchAdmin(admin.ModelAdmin):
    pass
