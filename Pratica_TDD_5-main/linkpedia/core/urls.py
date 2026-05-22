from django.urls import path
from core.views import login, logout, home
from core.views import cadastrar_link, listar_links,selecionar_link ,atualizar_link, deletar_link, selecionar_delete

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('', home, name='home'),
    path('cadastrar_link/', cadastrar_link, name='cadastrar_link'),
    path('listar_links/', listar_links, name='listar_links'),
    path('selecionar_link/', selecionar_link, name='selecionar_link'),
    path('atualizar_link/<int:id>/', atualizar_link, name='atualizar_link'),
    path('deletar_link/<int:id>/', deletar_link, name='deletar_link'),
    path('selecionar_delete/', selecionar_delete, name='selecionar_delete'),
]