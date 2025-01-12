from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("brian",views.brian,name="brian"),
    path("<str:name>", views.greet,name="greet"),
    path("david",views.david,name="david"),
]
