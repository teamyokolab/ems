from django.core.exceptions import ObjectDoesNotExist
from . models import User
from django.db.models import Q
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

	#login確認処理
	def login_check(request):
		try:
			if request.session['user_name']:
				return True
		except (KeyError):
			return False
	
	#userデータ取得処理 指定したnameとuser_nameが一致する情報を返す
	def get_user(self, name):
		try:
			user = User.objects.get(user_name = name)
			return user
		except ObjectDoesNotExist:
			return False

	def create_user(self, name, password, authority):
		user = User(user_name=name, user_password=password, user_authority=authority, delete_flag=0)
		user.save()

	# user_list を返す関数
	def get_user_list(authority, name):
		if authority == 2 | authority == 3:
			users = User.objects.filter(delete_flag=0).filter(Q(user_authority=1)| Q(user_authority=2))
		if authority == 1:
			users = User.objects.filter(user_name=name)
		return users
