from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#from . import views
#from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('U_user/', include('base.urls')),
    path('api/', include('base.urls')),
    path('roles/', include('base.urls')),
    path('permissions/', include('base.urls')),
    path('internalusers/', include('base.urls')),
    path('rolepermissions/', include('base.urls')),
    path('metausers/', include('base.urls')),

    path('Property_Owner_meta/', include('base.urls')),
    path('Property_Owner/', include('base.urls')),
    path('Property/', include('base.urls')),
    path('Property_meta/', include('base.urls')),
    path('Property_Bills/', include('base.urls')),
    path('Bills/', include('base.urls')),
    path('Sector/', include('base.urls')),
    path('Zone/', include('base.urls')),
    path('Society/', include('base.urls')),
    path('Property_Type/', include('base.urls')),




    #path('roles/', include('base.urls')),
    #path('internalusers/', include('base.urls')),

    #path('', views.default_view),
    #path('api/', views.api_view, name='api'),
    #path('', views.default_view),  # Default view for the root path
    #path('', RedirectView.as_view(url='/api/'))
]

'''from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Define a URL pattern for the empty path
    # Other URL patterns
]'''

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('U_user/', include('myapp.urls')),  # Assuming 'U_user/' is your app's base path
    path('api/', include('myapp.urls')),  # Include the base path for your API endpoints
    # Add other URL patterns as needed
]'''
