from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application

        fields = [
            'id',
            'job',
            'applicant',
            'cover_letter',
            'status',
            'applied_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'applicant',
            'status',
            'applied_at',
            'updated_at',
        ]


# New serializer for recruiter status updates

class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'status']
        read_only_fields = ['id']