from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm


from rest_framework import generics
from .models import U_user, role, permission, Internal_User, role_permission, user_meta
from .serializers import U_userSerializer, RoleSerializer, PermissionSerializer, InternalUserSerializer, RolePermissionSerializer, MetaUserSerializer

from .models import Property_Owner_meta, Property_Owner, Property, Property_meta, Property_Bills, Bills, Sector, Zone, Society, Property_Type
from .serializers import Property_OwnerSerializer, Property_Owner_metaSerializer, PropertySerializer, Property_metaSerializer, Property_BillsSerializer, BillsSerializer, SectorSerializer, SocietySerializer, ZoneSerializer, Property_TypeSerializer

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = None

    topics = None
    room_count = None
    room_messages = None

    context = {'topics': topics,
               'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)




def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = None
    room_messages = None
    topics = None
    context = {'user': user, 'rooms': rooms,
               'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})




# Corrected import statement in studybud/urls.py
#from base import views



# views.py in one of your Django apps

class U_userCreateAPIView(generics.ListCreateAPIView):
    queryset = U_user.objects.all()
    serializer_class = U_userSerializer


class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer

class RoleRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer

class PermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = permission.objects.all()
    serializer_class = PermissionSerializer

class InternalUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Internal_User.objects.all()
    serializer_class = InternalUserSerializer

class RolePermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = role_permission.objects.all()
    serializer_class = RolePermissionSerializer

class MetaUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = user_meta.objects.all()
    serializer_class = MetaUserSerializer




class PropertyOwnerListCreatAPIView(generics.ListCreateAPIView):
    queryset = Property_Owner.objects.all()
    serializer_class = Property_OwnerSerializer
class PropertyOwnerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_Owner.objects.all()
    serializer_class = Property_OwnerSerializer

class PropertyOwnermetaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_Owner_meta.objects.all()
    serializer_class = Property_Owner_metaSerializer
class PropertyOwnermetaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_Owner_meta.objects.all()
    serializer_class = Property_Owner_metaSerializer


class PropertyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
class PropertyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertymetaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_meta.objects.all()
    serializer_class = Property_metaSerializer
class PropertymetaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_meta.objects.all()
    serializer_class = Property_metaSerializer


class PropertyBillsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_Bills.objects.all()
    serializer_class = Property_BillsSerializer
class PropertyBillsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer

class BillsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
class BillsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer


class SectorListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
class SectorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer


class ZoneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
class ZoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer


class SocietyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
class SocietyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer


class PropertyTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
class PropertyTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer


