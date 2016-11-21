from django.shortcuts import render
from . account import Account
# Create your views here.

def index(request):
	return render(request, 'login.html')

def menu(request):
	try:
		#フォームからの入力を保存
		name = request.POST['user_name']
		password = request.POST['password']
		#アカウントオブジェクトを作成(account.py参照)
		account = Account()
		#ログイン処理(True->SESSTIONへ情報保存)
		if account.login(name, password):
			#user_name = nameのユーザ情報を取得
			user = account.get_user(name)
			#sessionにユーザ名と権限を保存
			request.session['user_name'] = user.user_name
			request.session['user_authority'] = user.user_authority
			#権限により繊維先を振り分ける
			if request.session['user_authority'] != 3:
				menu_path = 'menu.html'
			else:
				menu_path = 'admin_menu.html'
			return render(request, menu_path, {
				'authority': request.session['user_authority']
			})
		else:
			return render(request, 'error.html', {
				'page' : 'index'
			})
	except (KeyError):
		return render(request, 'error.html', {
			'page' : 'index'
		})
