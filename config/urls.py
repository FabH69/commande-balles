from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("deconnexion/", auth_views.LogoutView.as_view(next_page="/"), name="deconnexion"),
    path("", include("commandes.urls")),
]
