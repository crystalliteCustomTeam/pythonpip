from django.urls import path
from . import views,admin,include

urlpatterns = [
    path('',  views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),

   ''' path('admin/', admin.site.urls),
    path('U_user/', include('base.urls')),
    path('api/', include('base.urls')),
    path('roles/', include('base.urls')),
    path('permissions/', include('base.urls')),
    path('internalusers', include('base.urls')),
    path('rolepermissions', include('base.urls')),
    path('metausers', include('base.urls')),
    path('', views.default_view),'''

]