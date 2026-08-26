from django.contrib import admin
from .models import Part, StockOperation

admin.site.register(Part)
admin.site.register(StockOperation)
