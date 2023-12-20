from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    #path('/home', views.home, name="home"),
    path('import', views.import_excel, name="import-excel"),
]
