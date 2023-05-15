from rest_framework.views import APIView, Response,status
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TasksSerializer, UserSerializer

class ListarCriarTask(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        tarefas = Task.objects.filter(usuario = request.user)
        print(tarefas)
        serializer = TasksSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['usuario'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalheAtualizarRemoverTask(APIView):

    permission_classes = [IsAuthenticated]

    def get_tarefa(self, pk, usuario):
        try:
            return Task.objects.get(pk=pk, usuario=usuario)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tarefa = self.get_tarefa(pk, request.user)
        serializer = TasksSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):
        tarefa = self.get_tarefa(pk, request.user)
        serializer = TasksSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = self.get_tarefa(pk, request.user)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ListSituacaoNivelPrioridade(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = TasksSerializer
    print(1)
    
    def get_queryset(self):

        user = self.request.user
        queryset = Task.objects.filter(usuario = user)
        print(queryset)
        nivel = self.request.query_params.get('nivel')
        situacao = self.request.query_params.get('situacao')
        prioridade = self.request.query_params.get('prioridade')
        if nivel:
            queryset = queryset.filter(nivel=nivel)
        if situacao:
            queryset = queryset.filter(situacao=situacao)
        if prioridade:
            queryset = queryset.filter(prioridade=prioridade)
        return queryset
    def list(self, request, *args, **kwargs):
        user = self.request.user
        queryset = self.get_queryset().filter(usuario = user)
        if not queryset.exists():
            return Response({"detail": "Nenhum resultado encontrado."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

