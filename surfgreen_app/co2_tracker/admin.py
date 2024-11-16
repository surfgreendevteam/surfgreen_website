from django.contrib import admin
from surfgreen_app.co2_tracker.models import CO2Data
# Register your models here.
@admin.register(CO2Data)
class CO2DataAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'emissions', 'path', 'timestamp')
    search_fields = ('session_id', 'path')