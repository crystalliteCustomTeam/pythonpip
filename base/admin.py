from django.contrib import admin

# Register your models here.

from .models import Topic, Message, User, U_user, Internal_User, user_meta, role, permission, role_permission
from .models import Property_Owner_meta, Property_Owner, Property, Property_meta, Property_Bills, Bills, Sector, Zone, Society, Property_Type


admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(U_user)
admin.site.register(Internal_User)
admin.site.register(user_meta)
admin.site.register(role)
admin.site.register(permission)
admin.site.register(role_permission)

admin.site.register(Property_Owner_meta)
admin.site.register(Property_Owner)
admin.site.register(Property)
admin.site.register(Property_meta)
admin.site.register(Property_Bills)
admin.site.register(Bills)
admin.site.register(Sector)
admin.site.register(Zone)
admin.site.register(Society)
admin.site.register(Property_Type)

