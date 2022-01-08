from .models import Secret_Messages
from rest_framework import serializers

class SecretMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret_Messages
        fields = ['id','recipient','message','date']