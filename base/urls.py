from django.urls import path
from . import views
from .views import  *
# 1 line up

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('update-user/', views.updateUser, name="update-user"),

]


urlpatterns = [
    path('U_user/',  U_userCreateAPIView.as_view(), name='U_user-list-create'),
    path('roles/', RoleListCreateAPIView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleRetrieveUpdateAPIView.as_view(), name='role-detail-update'),
    path('permissions/', PermissionListCreateAPIView.as_view(), name='permission-list-create'),
    path('permissions/<int:pk>/', PermissionRetrieveUpdateAPIView.as_view(), name='permissions-detail-update'),
    # path('/permissions/', PermissionListCreateAPIView.as_view(), name='set-permission-list-create'),
    path('internalusers/', InternalUserListCreateAPIView.as_view(), name='internaluser-list-create'),
    path('rolepermissions/', RolePermissionListCreateAPIView.as_view(), name='rolepermission-list-create'),
    path('metausers/', MetaUserListCreateAPIView.as_view(), name='metauser-list-create'),
]
