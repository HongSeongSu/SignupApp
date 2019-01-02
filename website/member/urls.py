from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='home'),
    path('step1', views.step1view, name='step1'),
    path('step2', views.step2view, name='step2'),
    path('step3', views.step3view, name='step3'),
    path('step4', views.step4view, name='step4'),
]
