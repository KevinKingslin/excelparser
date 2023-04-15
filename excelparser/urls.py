from django.urls import path

from . import views

urlpatterns = [
    # View routes
    path("", views.index, name="index"),

    path("addProducts", views.addProducts, name="addProducts")
]
