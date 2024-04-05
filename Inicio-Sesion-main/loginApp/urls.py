from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
     path('logout/', include('logout.urls')),
    path('accounts/', include('accounts.urls')), # Apéndice 
]
