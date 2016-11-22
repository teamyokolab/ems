from django.shortcuts import render
from . account import Account
# Create your views here.

#login画面
def index(request):
	return render(request, 'login.html')

#menu画面
def menu(request):
	try:
		if request.session['user_name']:
			if request.session['user_authority'] != 3:
				menu_path = 'menu.html'
			else:
				menu_path = 'admin_menu.html'
		
			return render(request, menu_path, {
				'authority' : request.session['user_authority']
			})
	except (KeyError):
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

#ユーザ登録画面
def create(request):
	return render(request, 'user_create.html')

#ユーザ登録完了画面
def user_comp(request):
	name = request.POST['user_name']
	password = request.POST['user_password']
	authority = request.POST['authority']
	account = Account()
	account.create_user(name, password, authority)
	return render(request, 'comp.html')

def eq_search(request):
	return render(request,'eq_search.html')
