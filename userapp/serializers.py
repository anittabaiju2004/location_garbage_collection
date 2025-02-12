from rest_framework import serializers
from .models import tbl_register

class userregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_register
        fields = '__all__'


from rest_framework import serializers
from .models import ComplaintRegister

from rest_framework import serializers
from .models import ComplaintRegister

class ComplaintRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintRegister
        fields = '__all__'
        read_only_fields = ['status', 'date']
