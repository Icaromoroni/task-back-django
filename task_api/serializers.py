from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()


CHOICE_SITUACAO =  [('Nova','Nova'),
                    ('Em andamento','Em andamento'),
                    ('Pendente', 'Pendente'),
                    ('Resolvida','Resolvida'),
                    ('Cancelada','Cancelada')]

class TasksSerializer(serializers.ModelSerializer):

    usuario = serializers.ReadOnlyField(source='usuario.username')

    descricao = serializers.CharField()
    situacao = serializers.ChoiceField(choices=CHOICE_SITUACAO)
    responsavel = serializers.CharField(max_length=250, default='')

    def validate_descricao(self, value):
        return value.capitalize()
    
    # def validate_situacao(self, value):
    #     return value.capitalize()
    
    def validate_responsavel(self, value):
        return value.capitalize()

    class Meta:
        
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user