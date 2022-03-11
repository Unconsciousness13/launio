from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('launio.club.urls')),
    path('accounts/', include('launio.accounts.urls')),
)
