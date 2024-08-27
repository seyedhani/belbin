from django.db import models
import datetime
class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_numb =models.CharField(max_length=20)
    first_name = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    score =models.IntegerField()
    def __str__(self):
        return F'{self.first_name}{self.last_name}'
    
class Questions(models.Model):
    numb = models.IntegerField()
    url = models.CharField( max_length=50)
    ques = models.CharField(max_length=500)
    def __str__(self):
        return F'{self.numb}{self.ques}'
    
class MainQ(models.Model):
    title = models.CharField(max_length=300)
    def __str__(self) :
        return self.title
class AggrQ(models.Model):
    main_q = models.ForeignKey(MainQ , on_delete=models.CASCADE ,related_name='part' )
    qtext = models.CharField(max_length=400)
    def __str__(self) :
        return self.qtext
   
 
 