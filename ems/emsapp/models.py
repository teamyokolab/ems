from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
# Create your models here.

class User(models.Model):
	user_id = models.AutoField(primary_key=True, unique=True)
	user_name = models.CharField(max_length=8, unique=True, validators=[MinLengthValidator(4)])
	user_password = models.CharField(max_length=32, validators=[MinLengthValidator(8)])
	AUTHORITY_CHOICES = (
		('1', '学生'),
		('2', '教員'),
		('3', '管理者')
	)
	user_authority = models.IntegerField(choices=AUTHORITY_CHOICES)
	create_date = models.DateField(auto_now_add=True)
	DELETE_FLAG_CHOICES = (
		('0', '未削除'),
		('1', '削除')
	)
	delete_flag = models.IntegerField(choices=DELETE_FLAG_CHOICES)

class Equipment(models.Model):
	eq_id = models.AutoField(primary_key=True, unique=True)
	owner_user = models.ForeignKey(User)
	eq_name = models.CharField(max_length=32, validators=[MinLengthValidator(8)])
	CATEGORY_CHOICES = (
		('PC', 'PC'),
		('周辺機器', '周辺機器'),
		('ソフトウェア', 'ソフトウェア'),
		('事務用品', '事務用品'),
		('電化製品', '電化製品'),
		('家具', '家具'),
		('書籍', '書籍'),
		('消耗品', '消耗品'),
		('その他', 'その他')
	)
	eq_category = models.CharField(max_length=12, choices=CATEGORY_CHOICES)
	purchase_date = models.DateField()
	disposal_date = models.DateField()
	DISPOSAL_FLAG_CHOICES = (
		('0', '未削除'),
		('1', '削除')
	)
	disposal_flag = models.IntegerField(choices=DISPOSAL_FLAG_CHOICES)
