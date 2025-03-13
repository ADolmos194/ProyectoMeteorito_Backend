from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings
from django.template.defaulttags import url
from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
