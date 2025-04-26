from django.contrib import admin
from django.urls import path
from store.views import home
from django.conf import settings
from django.conf.urls.static import static
from store import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)