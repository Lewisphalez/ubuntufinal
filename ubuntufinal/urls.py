

from django.contrib import admin
from django.urls import path,include

import ubuntufinalapp

urlpatterns = [
    path('admin/', admin.site.urls),
path('', include('ubuntufinalapp.urls')),
path('fundraisers/', include('fundraisers.urls')),
path('accounts/', include('accounts.urls')),




]
