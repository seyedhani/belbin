from django.db import models
from django.contrib.auth.models import User
import datetime
class MainQ(models.Model):
    title = models.CharField(max_length=300)
    def __str__(self) :
        return self.title
class AggrQ(models.Model):
    main_q = models.ForeignKey(MainQ , on_delete=models.CASCADE ,related_name='part' )
    qtext = models.CharField(max_length=400)
    def __str__(self) :
        return self.qtext
        return self.title
class ScoreForm(models.Model):
    main_q = models.ForeignKey(MainQ , on_delete=models.CASCADE )
    part_q = models.ForeignKey(AggrQ , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    Score = models.IntegerField()
  