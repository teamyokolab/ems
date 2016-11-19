from django.shortcuts import render
from . account import Account
from . models import User
from django.db.models import Q
from . models import Equipment
from datetime import date
from . equipment import EditEquipment
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
def user_regist(request):
	return render(request, 'user_regist.html')

#ユーザ登録完了画面
def user_regist_comp(request):
	name = request.POST['user_name']
	password = request.POST['user_password']
	authority = request.POST['authority']
	account = Account()
	account.create_user(name, password, authority)
	return render(request, 'comp.html')

#ユーザ一覧画面
def user_list(request):
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request, 'user_list.html', {
		'user' : users
	})

#ユーザ削除画面
def user_delete(request):
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request, 'user_delete.html', {
		'user' : users
	})
#ユーザ削除完了画面
def user_delete_comp(request):
	delete_users = request.POST.getlist('delete_users')
	users = User.objects.filter(user_id__in=delete_users)
	users.update(delete_flag='1')
	return render(request, 'comp.html')

#ユーザ復元画面
def user_restore(request):
	delete_users = User.objects.filter(delete_flag=1)
	return render(request, 'user_restore.html', {
		'users' : delete_users
	})

#ユーザ復元完了
def user_restore_comp(request):
	restore_users = request.POST.getlist('restore_users')
	users = User.objects.filter(user_id__in=restore_users)
	users.update(delete_flag=0)
	return render(request, 'comp.html')
#備品登録画面
def eq_regist(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request,'eq_regist.html',{
		'user_list': users
	})

#備品登録完了画面
def eq_regist_comp(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	name = request.POST['eq_name']
	category = request.POST['category']
	owner = request.POST['owner']
	year = request.POST['year']
	month = request.POST['month']
	day = request.POST['day']
	pur_date = year+'-'+month+'-'+day
	account = Account()
	owner_id = account.get_user(owner)
	EditEquipment.regist_equipment(name, owner_id, category, pur_date)
	return render(request, 'comp.html')	

#備品検索画面
def eq_search(request):
	try:
		if request.session['user_name']:
			users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
			return render(request,'eq_search.html',{
				'user_list': users
			})
	except (KeyError):
		return render(request, 'error.html', {
				'page' : 'index'
				})
#備品検索結果画面
def eq_list(request):
	return render(request,'eq_list.html')

#備品廃棄用検索画面
def eq_disposal_search(request):
	try:
		if request.session['user_name']:
			users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
			return render(request,'eq_disposal_search.html',{
					'user_list': users
				})
	except (KeyError):
			return render(request, 'error.html', {
					'page' : 'index'
				})
#備品廃棄用検索結果表示
def eq_disposal(request):
	return render(request,'eq_disposal.html')

#備品復元用検索画面
def eq_restore_search(request):
	try:
		if request.session['user_name']:
			users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
			return render(request,'eq_restore_search.html',{
					'user_list': users
					})
	except (KeyError):
		return render(request, 'error.html', {
			'page' : 'index'
			})

#備品復元用検索結果画面
def eq_restore(request):
	return render(request,'eq_restore.html')

#ログアウト
def logout(request):
	del request.session['user_name']
	del request.session['user_authority']
	return render(request, 'login.html')
