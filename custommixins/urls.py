from django.contrib import admin
from django.urls import path , include
from djangomixin import views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:id>/' , views.PageView.as_view(),name='pageview'),
    path('api/' , include(router.urls))
]





