from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('launio.club.urls')),
                  path('accounts/', include('launio.accounts.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'launio.accounts.views.handler400'
handler403 = 'launio.accounts.views.handler403'
handler404 = 'launio.accounts.views.handler404'
handler500 = 'launio.accounts.views.handler500'
