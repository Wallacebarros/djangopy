#from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("App_Two/", include("App_Two.urls")),
    #path("admin/", admin.site.urls),
]