from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Shift, Man, Machine, Material, Method, MachineUsage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'name', 'start_time', 'end_time']

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'name', 'type', 'status']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'category']

class ManSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    shift = serializers.PrimaryKeyRelatedField(queryset=Shift.objects.all())
    machines = serializers.PrimaryKeyRelatedField(queryset=Machine.objects.all(), many=True)

    class Meta:
        model = Man
        fields = ['id', 'user', 'name', 'email', 'phone_no', 'role', 'shift', 'machines']

class MethodSerializer(serializers.ModelSerializer):
    responsible_man = serializers.PrimaryKeyRelatedField(queryset=Man.objects.all())
    machines = serializers.PrimaryKeyRelatedField(queryset=Machine.objects.all(), many=True)
    materials = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all(), many=True)

    class Meta:
        model = Method
        fields = ['id', 'name', 'description', 'responsible_man', 'machines', 'materials']

class MachineUsageSerializer(serializers.ModelSerializer):
    man = serializers.PrimaryKeyRelatedField(queryset=Man.objects.all())
    machine = serializers.PrimaryKeyRelatedField(queryset=Machine.objects.all())
    method = serializers.PrimaryKeyRelatedField(queryset=Method.objects.all())

    class Meta:
        model = MachineUsage
        fields = ['id', 'man', 'machine', 'method', 'start_time', 'end_time']

