from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('general_statistics', views.general_statistics, name='general_statistics'),
    path('demand_page', views.demand_page, name='demand_page'),
    path('geography_statistics', views.geography_statistics, name='geography_statistics'),
    path('skills_statistics', views.skills_statistics, name='skills_statistics'),
    path('latest_vacancies', views.latest_vacancies, name='latest_vacancies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
