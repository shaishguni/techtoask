from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
# from Main import urls
import os
from Project.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Main.urls"))
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Tech To Ask"
admin.site.site_title = "Tech Group.inc"
admin.site.index_title = ""
