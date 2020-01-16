from developers import models, serializers
from rest_framework import viewsets
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


class DeveloperViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeveloperSerializer

    def get_queryset(self):
        queryset = models.Developer.objects.all().order_by('name')
        username = self.request.query_params.get('github_username', None)
        techs = self.request.query_params.get('techs', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        if username:
            queryset = queryset.filter(github_username__icontains=username)
        if techs:
            techs_array = [tech.strip() for tech in techs.split(',')]
            for tech in techs_array:
                queryset = queryset.filter(techs__icontains=tech)
        if latitude and longitude:
            point = Point(float(longitude), float(latitude))
            queryset = queryset.filter(location__distance_lt=(point, Distance(km=10000)))
        return queryset
