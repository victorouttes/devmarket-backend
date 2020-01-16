from developers import models, serializers
from rest_framework import viewsets


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = models.Developer.objects.all().order_by('name')
    serializer_class = serializers.DeveloperSerializer
