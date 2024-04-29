from rest_framework.serializers import ModelSerializer


class RoomSerializer(ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'

