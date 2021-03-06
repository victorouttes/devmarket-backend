import json
import requests
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField

from developers import models


#  Custom field representing tech attribute, wich is a string in database and a array string externally.
class TechCustomField(serializers.ListField):
    child = serializers.CharField(min_length=1)

    def __init__(self, *args, **kwargs):
        super(TechCustomField, self).__init__(*args, **kwargs)

    #  output representation of attribute tech
    def to_representation(self, data):
        return json.loads(data)

    #  internal representation of attribute tech
    def to_internal_value(self, data):
        return json.dumps(data)


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    techs = TechCustomField(required=False, default=[], allow_null=True)
    location = PointField(required=False, allow_null=True)

    def create(self, validated_data):
        github_user = validated_data.get('github_username')

        try:
            dev = models.Developer.objects.get(github_username=github_user)
            return dev
        except models.Developer.DoesNotExist:
            gituser = requests.get('https://api.github.com/users/{}'.format(github_user)).json()

            if 'message' in gituser:
                return super(DeveloperSerializer, self).create(validated_data)

            if not gituser['name']:
                gituser['name'] = gituser['login']

            if 'name' in validated_data:
                validated_data.pop('name')
            if 'bio' in validated_data:
                validated_data.pop('bio')
            if 'avatar_url' in validated_data:
                validated_data.pop('avatar_url')
            data = {
                'name': gituser['name'],
                'bio': gituser['bio'],
                'avatar_url': gituser['avatar_url'],
                **validated_data
            }
            return super(DeveloperSerializer, self).create(data)

    class Meta:
        model = models.Developer
        fields = '__all__'
