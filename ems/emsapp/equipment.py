from django.core.exceptions import ObjectDoesNotExist
from . models import Equipment
from . models import User
from django.db.models import Q
class EditEquipment:
	def regist_equipment(name, owner_id, category, pur_date):
		equipment = Equipment(eq_name=name, owner_user=owner_id, eq_category=category, purchase_date=pur_date, disposal_flag=0)
		equipment.save()

	def change_flag(eq, flag):
		equipment = Equipment.objects.filter(eq_id__in=eq)
		equipment.update(disposal_flag=flag)
	

class Search:

	def search(request, flag):
		category = request.POST['category']
		owner = User.objects.get(user_name=request.POST['owner'])
		owner_id = owner.user_id
		pur_year = None
		pur_month = None
		dip_year = None
		dip_month = None
		try:
			pur_year = request.POST['pur_year']
			pur_month = request.POST['pur_month']
			dip_year = request.POST['dip_year']
			dip_month = request.POST['dip_month']
		except KeyError:
			pass
		equipments = Search.get_eq_list(pur_year, pur_month, dip_year, dip_month, category, owner_id, flag);
		return equipments

	def get_eq_list(pur_year, pur_month, dip_year, dip_month, category, owner_id, flag):
		if pur_year is not None and dip_year is not None:
			equipments = Equipment.objects.filter(purchase_date__year=pur_year).filter(purchase_date__month=pur_month)\
			.filter(disposal_date__year=dip_year).filter(disposal_date__month=dip_month).filter(eq_category=category).filter(owner_user_id=owner_id).filter(disposal_flag=flag)
		elif pur_year is not None and dip_year is None:
			equipments = Equipment.objects.filter(purchase_date__year=pur_year).filter(purchase_date__month=pur_month)\
			.filter(eq_category=category).filter(owner_user_id=owner_id).filter(disposal_flag=flag)
		elif pur_year is None and dip_year is not None:
			equipments = Equipment.objects.filter(disposal_date__year=dip_year).filter(disposal_date__month=dip_month)\
			.filter(eq_category=category).filter(owner_user_id=owner_id).filter(disposal_flag=flag)
		else:
			equipments = Equipment.objects.filter(eq_category=category).filter(owner_user_id=owner_id).filter(disposal_flag=flag)
		return equipments

