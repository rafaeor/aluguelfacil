from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('painel/', views.painel_proprietario, name='painel_proprietario'),
    path('painel/novo-imovel/', views.create_imovel, name='create_imovel'),
    path('painel/<int:imovel_id>/vincular/', views.vincular_inquilino, name='vincular_inquilino'),
    path('minha-casa/', views.painel_inquilino, name='painel_inquilino'),
    path('pagar/<int:pagamento_id>/', views.pagar_pix, name='pagar_pix'),
    path('imovel/<int:imovel_id>/', views.detalhe_imovel, name='detalhe_imovel'),
]
