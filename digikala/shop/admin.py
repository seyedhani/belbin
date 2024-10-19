from django.contrib import admin
from . import models
admin.site.register(models.MainQ)
admin.site.register(models.AggrQ)
admin.site.register(models.ScoreForm)
admin.site.register(models.Result)
admin.site.register(models.SuperUser)
