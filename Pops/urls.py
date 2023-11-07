from django.contrib import admin
from django.urls import path
from Pops import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pops/', views.pop_list),
    path('pops/<int:id>', views.pop_detail)
]

"""this function allows the capabilities to have different url extension e.g pops.json"""
urlpatterns = format_suffix_patterns(urlpatterns)