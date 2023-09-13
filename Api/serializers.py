from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id","name"]

    def __init__(self, *args, **kwargs):
        super(PersonSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

