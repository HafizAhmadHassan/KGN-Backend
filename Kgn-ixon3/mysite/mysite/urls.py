
from django.contrib import admin
from django.urls import path,include

admin.site.site_header= " KGN Web Portal "
admin.site.site_title= " KGN Portal "
admin.site.index_title= " KGN || Admin Panel"

urlpatterns = [
    path('kgnWebApp/',include("kgnWebApp.urls")),
    path('admin/', admin.site.urls),
]
