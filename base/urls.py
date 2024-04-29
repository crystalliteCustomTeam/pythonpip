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



    path('Property_Owner_meta/', PropertyOwnermetaListCreateAPIView.as_view(), name='Property_Owner_meta-list-create'),
    path('property_owners_meta/<int:pk>/', PropertyOwnermetaRetrieveUpdateDestroyAPIView.as_view(), name='Property_Owner_meta-detail'),

    path('Property_Owner/', PropertyOwnerListCreatAPIView.as_view(), name='Property_Owner-list-create'),
    path('property_owners/<int:pk>/', PropertyOwnerRetrieveUpdateDestroyAPIView.as_view(), name='Property_Owner-detail'),

    path('Property/', PropertyListCreateAPIView.as_view(), name='Property-list-create'),
    path('property/<int:pk>/', PropertyRetrieveUpdateDestroyAPIView.as_view(), name='Property-detail'),
    
    path('Property_meta/', PropertymetaListCreateAPIView.as_view(), name='Property_meta-list-create'),
    path('property_meta/<int:pk>/', PropertymetaRetrieveUpdateDestroyAPIView.as_view(), name='Property_meta-detail'),
    
    path('Property_Bills/', PropertyBillsListCreateAPIView.as_view(), name='Property_Bills-list-create'),
    path('property_bills/<int:pk>/', PropertyBillsRetrieveUpdateDestroyAPIView.as_view(), name='Property_Bills-detail'),
    
    path('Bills/', BillsListCreateAPIView.as_view(), name='Bills-list-create'),
    path('Bills/<int:pk>/', BillsRetrieveUpdateDestroyAPIView.as_view(), name='Bills-detail'),

    path('Sector/', SectorListCreateAPIViews.as_view(), name='Sector-list-create'),
    path('sector/<int:pk>/', SectorRetrieveUpdateDestroyAPIView.as_view(), name='Sector-detail'),
    
    path('Zone/', ZoneListCreateAPIView.as_view(), name='Zone-list-create'),
    path('zone/<int:pk>/', ZoneRetrieveUpdateDestroyAPIView.as_view(), name='Zone-detail'),

    path('Society/', SocietyListCreateAPIView.as_view(), name='Society-list-create'),
    path('society/<int:pk>/', SocietyRetrieveUpdateDestroyAPIView.as_view(), name='Society-detail'),
    
    path('Property_Type', PropertyTypeListCreateAPIView.as_view(), name='Property_Type-create-list'),
    path('property_type/<int:pk>/', PropertyTypeRetrieveUpdateDestroyAPIView.as_view(), name='Property_Type-detail'),



]
