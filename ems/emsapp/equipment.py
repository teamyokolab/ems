from django.core.exceptions import ObjectDoesNotExist
from . models import Equipment
from . models import User
from django.db.models import Q
class EditEquipment:
	def regist_equipment(name, owner_id, category, pur_date):
		equipment = Equipment(eq_name=name, owner_user=owner_id, eq_category=category, purchase_date=pur_date, disposal_flag=0)
		equipment.save()

	def get_eq_list(pur_year, pur_month, dip_year, dip_month, category, owner_id):
		if pur_year is not None and dip_year is not None:
			equipments = Equipment.objects.filter(purchase_date__year=pur_year).filter(purchase_date__month=pur_month).filter(disposal_date__year=dip_year).filter(disposal_date__month=dip_month).filter(eq_category=category).filter(owner_user_id=owner_id)
		elif pur_year is not None and dip_year is None:
			equipments = Equipment.objects.filter(purchase_date__year=pur_year).filter(purchase_date__month=pur_month).filter(eq_category=category).filter(owner_user_id=owner_id)
		elif pur_year is None and dip_year is not None:
			equipments = Equipment.objects.filter(disposal_date__year=dip_year).filter(disposal_date__month=dip_month).filter(eq_category=category).filter(owner_user_id=owner_id)
		else:
			equipments = Equipment.objects.filter(eq_category=category).filter(owner_user_id=owner_id)
		return equipments
