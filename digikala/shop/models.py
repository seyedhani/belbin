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
       
class ScoreForm(models.Model):
    main_q = models.ForeignKey(MainQ , on_delete=models.CASCADE )
    part_q = models.ForeignKey(AggrQ , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    Score = models.IntegerField()
  
class Result(models.Model):
    summery = models.CharField(max_length=1000)
    feature = models.CharField(max_length=1000)
    weakness = models.CharField(max_length=1000)
    powers = models.CharField(max_length=1000)
    
class SuperUser(models.Model):
    gender_choices=(
        ('man', 'man'),
        ('woman' , 'woman'),
        ('rather not to say' ,'rather not to say' ),
        
    )
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    result = models.ForeignKey(Result ,on_delete=models.CASCADE)
    phone_numb = models.CharField(max_length=12)
    gender =models.CharField(max_length=30 , choices=gender_choices ,default='man')
    date = models.DateField( default=datetime.date.today)
    def __str__(self) :
        return self.user_id.username
