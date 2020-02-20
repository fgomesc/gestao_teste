from django.urls import path
from .views import relatorio_funcionario
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioNovo,
    Pdf
)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('realtorio-funcionarios>/', relatorio_funcionario, name='relatorio_funcionario'),
    path('realtorio-funcionarios-html>/', Pdf.as_view(), name='relatorio_funcionario_html'),
]
