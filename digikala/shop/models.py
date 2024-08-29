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
class Account(models.Model):
    phone =models.CharField(max_length=250)
    
class Scores(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="score") 
    section = models.ForeignKey(MainQ ,  on_delete=models.CASCADE)
    question = models.ForeignKey(AggrQ ,  on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self) :
        return self.user.first_name 