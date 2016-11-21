from django.core.exceptions import ObjectDoesNotExist
from . models import User

class Account:
	def __init__(self):
		self.test = 'test'	
	
	def login(self, name, password):
		try:
			user_name = User.objects.get(user_name = name)
			user_password = User.objects.get(user_password = password)
			return True
		except ObjectDoesNotExist:
			return False
