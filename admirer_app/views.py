from rest_framework import viewsets
from admirer_app.models import Secret_Messages
from admirer_app.serializers import SecretMessagesSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class SecretMessageViewSet(viewsets.ModelViewSet):
    queryset = Secret_Messages.objects.all()
    serializer_class = SecretMessagesSerializer
    http_method_names = ['get', 'post']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['recipient']