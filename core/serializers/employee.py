from rest_framework import ModelSerializer
from core.models import Funcionario

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
        depth = 1