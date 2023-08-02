from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.product.urls')),
    path('blog/', include('apps.blog.urls')),
    path('register/', include('apps.user.urls')),
    path('cart/', include('apps.cart.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        # ...
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
