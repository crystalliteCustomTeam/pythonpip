from rest_framework import serializers
from .models import U_user, role, permission, Internal_User, role_permission, user_meta, Property_Owner_meta, Property_Owner, Property, Property_meta, Property_Bills, Bills, Sector, Zone, Society, Property_Type


class U_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = U_user
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = permission
        fields = '__all__'

class InternalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internal_User
        fields = '__all__'

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = role_permission
        fields = '__all__'

class MetaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_meta
        fields = '__all__'



class Property_Owner_metaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Owner_meta
        fields = '__all__'

class Property_OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Owner
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class Property_metaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_meta
        fields = '__all__'

class Property_BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Bills
        fields = '__all__'

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        fields = '__all__'

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

class Property_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Type
        fields = '__all__'