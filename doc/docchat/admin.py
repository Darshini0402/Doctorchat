from django.contrib import admin


from . import models

# Register your models here.

admin.site.register(models.user)
admin.site.register(models.doctor)
admin.site.register(models.patappointment)
admin.site.register(models.billing)
