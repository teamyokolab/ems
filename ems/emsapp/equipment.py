from django.core.exceptions import ObjectDoesNotExist
from . models import Equipment
from . models import User
from django.db.models import Q
class EditEquipment:
        def regist_equipment(name, owner_id, category, pur_date):
                equipment = Equipment(eq_name=name, owner_user=owner_id, eq_category=category, purchase_date=pur_date, disposal_flag=0)
                equipment.save()

