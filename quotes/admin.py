from django.contrib import admin

# Register your models here.
# quotes/admin.py
from .models import Quote

admin.site.register(Quote)
