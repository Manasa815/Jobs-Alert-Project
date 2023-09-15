from django.contrib import admin
from jobsapp.models import HydJobs,BangloreJobs,PuneJobs
class HydAdmin(admin.ModelAdmin):
    list_display=['role','positions','address','mail']
admin.site.register(HydJobs,HydAdmin)
class BangloreAdmin(admin.ModelAdmin):
    list_display=['role','positions','address','mail']
admin.site.register(BangloreJobs,BangloreAdmin)
class PuneAdmin(admin.ModelAdmin):
    list_display=['role','positions','address','mail']
admin.site.register(PuneJobs,PuneAdmin)