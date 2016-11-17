from django.db import models
from django import forms
# Create your models here.

class User(models.Model):
	usr_id = models.IntergerField()
	usr_name = models.CharField(max_length=8)
	password = models.CharField(max_length=8)
	permission = models.IntergerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
	reg_date = models.DateTimeField('date published')
	del_flag = models.IntergerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
 
class Equpment(models.Model):
	equ_id = models.IntergerField()
	equ_reg = models.CharField(max_length=8)
	equ_name = models.CharFiled()
	equ_kindof = models.CharField()
	reg_date = models.DateTimeField('date published')
	buy_date = models.DateTimeField('date published')
	del_date = models.DateTimeField('date published')
	del_flag = models.IntergerFielD(Validators=[MinValueValidator(0), MaxValueValidator(1)])

class UserForm(ModelForm):
	class Meta:
	model = User

class EqupmentForm(ModelForm):
	class Meta:
	model = Equpment
