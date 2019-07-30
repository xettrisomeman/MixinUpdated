
from django.contrib import admin
from django.urls import path
from djangomixin import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>/' , views.PageView.as_view(),name='pageview')
]
