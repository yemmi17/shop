from django.contrib import admin
from django.urls import path
from store.views import home
from django.conf import settings
from django.conf.urls.static import static
from store import views


urlpatterns = [
    path('fortunadmin/', admin.site.urls),
    path('', home, name='home'),
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('offer/', views.offer, name='offer'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'store.views.custom_404'
