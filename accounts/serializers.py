
from rest_framework import serializers
from .models import User, CandidateProfile, Skill
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
        ]

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class CandidateProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = CandidateProfile
        fields = '__all__'
        read_only_fields = [
            'user',
            'created_at',
            'updated_at',
        ]

    def validate_resume(self, value):
        import os
        allowed_extensions = ['.pdf', '.doc', '.docx']
        extension = os.path.splitext(value.name)[1].lower()
        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Only PDF, DOC and DOCX files are allowed."
            )
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError(
                "Resume file size must not exceed 5 MB."
            )
        return value


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password])

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'role',
        ]
        read_only_fields = ['id']

    def validate_role(self, value):
        if value not in [
            User.Role.JOB_SEEKER,
            User.Role.RECRUITER
        ]:
            raise serializers.ValidationError(
                "Invalid registration role."
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CandidateSkillsSerializer(serializers.ModelSerializer):
    skills = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Skill.objects.all()
    )

    class Meta:
        model = CandidateProfile
        fields = ['skills']


