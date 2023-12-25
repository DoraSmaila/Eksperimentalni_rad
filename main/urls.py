# main/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views
from .views import update_single_field,ProfesorList, ProfesorDetail, PredmetList, PredmetDetail,update_all_predmeti_for_profesor,read_profesori,read_predmeti,read_profesori_j_string,read_predmeti_j_string,read_profesori_j_type,read_predmeti_j_type

router = routers.DefaultRouter()
router.register(r'profesori', views.ProfesorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('update_single_field/<int:pk>/', update_single_field, name='update_single_field'),
    path('profesori/', ProfesorList.as_view(), name='profesor-list'),
    path('profesori/<int:pk>/', ProfesorDetail.as_view(), name='profesor-detail'),
    path('predmeti/', PredmetList.as_view(), name='predmet-list'),
    path('predmeti/<int:pk>/', PredmetDetail.as_view(), name='predmet-detail'),
    path('update_all_predmeti_for_profesor/<int:id>/', update_all_predmeti_for_profesor, name='update_all_predmeti_for_profesor'),
    path('read_profesori/', read_profesori, name='read_profesori'),
    path('read_predmeti/', read_predmeti, name='read_predmeti'),
    path('read_profesori_j_string/', read_profesori_j_string, name='read_profesori_j_string'),
    path('read_predmeti_j_string/', read_predmeti_j_string, name='read_predmeti_j_string'),
    path('read_profesori_j_type/', read_profesori_j_type, name='read_profesori_j_type'),
    path('read_predmeti_j_type/', read_predmeti_j_type, name='read_predmeti_j_type'),
]