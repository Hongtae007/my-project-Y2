from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('form',views.form),
    path('edit/<person_id>',views.edit),
    path('delete/<person_id>',views.delete),
    path('chart1',views.chart1),
    path('chart2',views.chart2),
    path('chart3',views.chart3),
    path('chart4',views.chart4)

]