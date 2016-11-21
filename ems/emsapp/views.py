from django.shortcuts import render
from . account import Account
# Create your views here.

def index(request):
	return render(request, 'login.html')

def menu(request):
	try:
		name = request.POST['user_name']
		password = request.POST['password']
		account = Account()
		if account.login(name, password):
			result = 'true'
		else:
			result = 'false'

		return render(request, 'menu.html', {
			'result': result
		})
	except (KeyError):
		return render(request, 'menu.html', {
			'result': 'KeyError'
		})
