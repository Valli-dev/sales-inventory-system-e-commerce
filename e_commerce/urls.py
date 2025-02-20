from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerceapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cartapp.urls')),
    path('payment/', include('payment.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
