from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import Livro
from core.serializers import LivroSerializer 

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroSerializer

    permission_classes = [IsAuthenticated]