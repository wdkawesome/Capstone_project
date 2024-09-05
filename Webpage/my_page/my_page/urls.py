from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', include('my_sites.urls')), 
    path('user/', include('user.urls')),
    path('reviews/', include('reviews.urls'))
]
