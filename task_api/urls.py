from django.urls import path
from .views import ListarCriarTask, DetalheAtualizarRemoverTask, ListSituacaoNivelPrioridade,UserSignup
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('tarefas/', ListarCriarTask.as_view(), name= 'listar-criar-tarefa'),
    path('tarefas/<int:pk>', DetalheAtualizarRemoverTask.as_view(), name='detalhar-atualizar-remover'),
    path('search/', ListSituacaoNivelPrioridade.as_view(), name='Situação-Nivel-Prioridade'),
    path('signup', UserSignup.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]