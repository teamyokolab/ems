from django.core.exceptions import ObjectDoesNotExist
from . models import User

class Account:
	#login認証処理	
	def login(self, name, password):
		try:
			user_info = User.objects.get(user_name = name)
			if user_info.user_password == password:
				return True
			else:
				return False
		except ObjectDoesNotExist:
			return False
	
	#userデータ取得処理 指定したnameとuser_nameが一致する情報を返す
	def get_user(self, name):
		try:
			user = User.objects.get(user_name = name)
			return user
		except ObjectDoesNotExist:
			return False
