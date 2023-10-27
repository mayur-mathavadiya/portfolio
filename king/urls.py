from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "MR Admin"
admin.site.site_title = "Mayur Mathavadiya Portal"
admin.site.index_title = "Welcome to Mayur Mathavadiya Portfolio"

urlpatterns = [
    path('', include('thor.urls')),
    path('admin/', admin.site.urls),
]