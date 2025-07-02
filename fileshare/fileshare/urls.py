from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your app URLs below
    # path('api/', include('core.urls')),  <-- if you have one
]
urlpatterns += [
    path('api/auth/', include('rest_framework.urls')),
]
