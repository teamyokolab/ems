from django.shortcuts import render
from . account import Account
from . models import User
from django.db.models import Q
from . models import Equipment
from django.shortcuts import get_object_or_404, render
from datetime import date
from . equipment import EditEquipment
from . equipment import Search
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
			#ログイン処理(True->SESSTIONへ情報保存)
			if Account.login(name, password):
				#user_name = nameのユーザ情報を取得
				user = Account.get_user(name)
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
	return render(request, 'user_regist.html', {
		'authority' : request.session['user_authority']
	})

#ユーザ登録完了画面
def user_regist_comp(request):
	name = request.POST['user_name']
	password = request.POST['user_password']
	authority = request.POST['authority']
	account = Account()
	result = account.create_user(name, password, authority)
	if result == True:
		return render(request, 'comp.html', {
			'authority' : request.session['user_authority']
		})
	else:
		return render(request, 'error.html', {
			'page' : 'menu'
		})

#ユーザ一覧画面
def user_list(request):
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request, 'user_list.html', {
		'user' : users,
		'authority' : request.session['user_authority']
	})

#ユーザ削除画面
def user_delete(request):
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request, 'user_delete.html', {
		'user' : users,
		'authority' : request.session['user_authority']
	})
#ユーザ削除完了画面
def user_delete_comp(request):
	delete_users = request.POST.getlist('delete_users')
	users = User.objects.filter(user_id__in=delete_users)
	users.update(delete_flag='1')
	return render(request, 'comp.html', {
		'authority' : request.session['user_authority']
	})

#ユーザ復元画面
def user_restore(request):
	delete_users = User.objects.filter(delete_flag=1)
	return render(request, 'user_restore.html', {
		'users' : delete_users,
		'authority' : request.session['user_authority']
	})

#ユーザ復元完了
def user_restore_comp(request):
	restore_users = request.POST.getlist('restore_users')
	users = User.objects.filter(user_id__in=restore_users)
	users.update(delete_flag=0)
	return render(request, 'comp.html', {
		'authority' : request.session['user_authority']
	})

#パスワード変更
def user_pass(request):
	users = User.objects.filter(delete_flag=0)
	return render(request, 'user_pass_change.html', {
		'user_list' : users,
		'authority' : request.session['user_authority']
	})

#パスワード変更完了
def user_pass_comp(request):
	name = request.POST['user_name']
	new_pass = request.POST['new_pass']
	user = User.objects.filter(user_name=name)
	user.update(user_password = new_pass)
	return render(request, 'comp.html', {
		'authority' : request.session['user_authority']
	})

#備品登録画面
def eq_regist(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request,'eq_regist.html',{
		'user_list': users,
		'authority' : request.session['user_authority']
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
	owner_id = User.objects.get(user_name=owner)
	EditEquipment.regist_equipment(name, owner_id, category, pur_date)
	return render(request, 'comp.html', {
		'authority' : request.session['user_authority']
	})	

#備品検索画面
def eq_search(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request,'eq_search.html',{
		'user_list': users,
		'page_title': '',
		'next_page' : 'eq_list',
		'authority' : request.session['user_authority']
	})

#備品検索結果画面
def eq_list(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	equipments = Search.search(request, 0)
	return render(request,'eq_list.html',{
		'equipments':equipments,
		'authority' : request.session['user_authority']
	})

#備品更新検索画面
def eq_update_search(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request, 'eq_search.html', {
		'user_list' : users,
		'page_title' : '(更新)',
		'next_page' : 'eq_update_list',
		'authority' : request.session['user_authority']
	})

#備品更新検索結果
def eq_update_list(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	equipments = Search.search(request, 0)
	return render(request, 'eq_update_list.html', {
		'equipments' : equipments,
		'authority' : request.session['user_authority']
	})

#備品更新内容入力
def eq_update(request, detail_id):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	eq = Equipment.objects.get(eq_id=detail_id)
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	user = request.session['user_name']
	category = eq.eq_category
	categorys = ['PC','周辺機器','ソフトウェア','事務用品','電化製品','家具','書籍','消耗品','その他']
	return render(request, 'eq_update.html', {
		'equipment' : eq,
		'user' : user,
		'users' : users,
		'categorys' : categorys,
		'category' : category,
		'authority' : request.session['user_authority']
	})
#備品更新完了
def eq_update_comp(request):
	if Account.login_check(request) == False:
		return rrender(request, 'error.html', {
			'page' : 'index'
		})
	update_id = request.POST['update_id']
	name = request.POST['name']
	category = request.POST['category']
	owner = request.POST['owner']
	owner_id = User.objects.get(user_name=owner).user_id
	eq = Equipment.objects.filter(eq_id=update_id)
	eq.update(eq_name=name, eq_category=category, owner_user_id=owner_id)
	return render(request, 'comp.html', {
		'authority' : request.session['user_authority']
	})


#備品廃棄用検索画面
def eq_disposal_search(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})		
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request, 'eq_search.html' ,{
		'user_list': users,
		'page_title': '(廃棄)',
		'next_page' : 'eq_disposal_list',
		'authority' : request.session['user_authority']
	})

#備品廃棄用検索結果表示
def eq_disposal_list(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	equipments = Search.search(request, 0)
	return render(request,'eq_check_list.html', {
		'equipments':equipments, 
		'flag' : 1,
		'next_page' : 'eq_disposal_comp',
		'action' : '廃棄',
		'authority' : request.session['user_authority']
	})
#備品廃棄完了画面
def eq_disposal_comp(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	eq = request.POST.getlist('eq_list')
	for id in eq :
		year = request.POST["year"+id]
		month = request.POST["month"+id]
		day = request.POST["day"+id]
		date = year + "-" + month + "-" + day
		dis_eq = Equipment.objects.filter(eq_id=id)
		dis_eq.update(disposal_date = date)
	
	EditEquipment.change_flag(eq, 1)
	return render(request, 'comp.html', {
		'authority' : request.session['user_authority']
	})
	
#備品復元用検索画面
def eq_restore_search(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})			
	users = Account.get_user_list(request.session['user_authority'], request.session['user_name'])
	return render(request,'eq_search.html',{
		'user_list': users,
		'page_title': '(復元)',
		'next_page' : 'eq_restore_list',
		'authority' : request.session['user_authority']				
	})

#備品復元用検索結果画面
def eq_restore_list(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	equipments = Search.search(request, 1)
	return render(request,'eq_check_list.html', {
		'equipments' : equipments,
		'flag' : 0,
		'next_page' : 'eq_restore_comp',
		'action' : '復元',
		'authority' : request.session['user_authority']
	})

#備品復元完了画面
def eq_restore_comp(request):
	if Account.login_check(request) == False:
		return render(request, 'error.html', {
			'page' : 'index'
		})
	eq = request.POST.getlist('eq_list')
	EditEquipment.change_flag(eq, 0)
	return render(request, 'comp.html', {
		'authority' : request.session['user_authority']
	})

#ログアウト
def logout(request):
	del request.session['user_name']
	del request.session['user_authority']
	return render(request, 'login.html')
