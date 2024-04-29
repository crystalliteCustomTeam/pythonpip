from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
    

class U_user(models.Model):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    role_ID = models.PositiveBigIntegerField(max_length=20)
    firstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    passwordHash = models.CharField(max_length=255)
    CNIC = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField(max_length=20)
    registered = models.DateTimeField()
    LastLogin = models.DateTimeField()


class Internal_User(models.Model):
    parent = models.ForeignKey(U_user, on_delete=models.CASCADE)
    id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    Emp_ID = models.PositiveBigIntegerField()
    CNIC = models.CharField(max_length=255)
    Data = models.TextField()
    is_active = models.BooleanField()
    Password = models.TextField()
    Created_at = models.TextField()
    updated = models.TextField()


class user_meta(models.Model):
    parent = models.ForeignKey(U_user, on_delete=models.CASCADE)
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    key = models.CharField(max_length=75) 
    value = models.CharField(max_length=75)
    used = models.PositiveBigIntegerField(max_length=20)


class role(models.Model):
    parent = models.ForeignKey(U_user, on_delete=models.CASCADE)
    id = models.PositiveBigIntegerField(max_length=20,primary_key=True)
    title = models.CharField(max_length=75)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    active = models.TextField(max_length=1)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()


class permission(models.Model):
    parent = models.ForeignKey(role, on_delete=models.CASCADE)
    id = models.PositiveBigIntegerField(max_length=20,primary_key=True)
    title = models.CharField(max_length=75)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    active = models.TextField(max_length=1) 
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()


class role_permission(models.Model):
    parent = models.ForeignKey(role, on_delete=models.CASCADE)
    roleId = models.PositiveBigIntegerField(max_length=20)
    permissionId = models.PositiveBigIntegerField(max_length=20)
    createdAT = models.DateTimeField()
    updatedAt = models.DateTimeField()


class Property_Owner(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Owner_Name = models.CharField(max_length=255)
    CNIC = models.CharField(max_length=255)
    Edit_by = models.BigIntegerField(max_length=20)
    Created_at = models.DateTimeField()
    Uploaded_at = models.DateTimeField()

class Property_Owner_meta(models.Model):
    ID = models.BigIntegerField(max_length=20)
    Key = models.CharField(max_length=255)
    Value = models.TextField()
    Owner_ID = models.PositiveBigIntegerField(max_length=20)
    Edit_by = models.PositiveBigIntegerField(max_length=20)

class Property(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Property_key = models.CharField(max_length=255)
    Sector = models.PositiveBigIntegerField(max_length=255)
    Owner = models.PositiveBigIntegerField(max_length=20)
    Property_Type = models.PositiveBigIntegerField(max_length=20)
    Plot_No = models.CharField(max_length=255)
    Society = models.PositiveBigIntegerField(max_length=20)
    Street_No = models.CharField(max_length=255)
    Phase = models.CharField(max_length=255)
    Gali_No = models.CharField(max_length=255)
    Society_Sector = models.CharField(max_length=255)
    Flat_No = models.CharField(max_length=255)
    Block_No = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField(max_length=20)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Property_meta(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Key = models.CharField(max_length=255)
    Value = models.TextField()
    Property_ID = models.PositiveBigIntegerField(max_length=20)
    Edit_by = models.PositiveBigIntegerField(max_length=20)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Property_Bills(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Consumer_ID = models.CharField(max_length=255)
    Bill_Type = models.PositiveBigIntegerField(max_length=20)
    Property_key = models.CharField(max_length=255)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Bills(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Name = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField(max_length=20)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Sector(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Name = models.CharField(max_length=255)
    Zone_ID = models.PositiveBigIntegerField(max_length=20)
    Created_by = models.PositiveBigIntegerField(max_length=20)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Zone(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Name = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField(max_length=20)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Society(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Image = models.TextField()
    Name = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField(max_length=20)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Property_Type(models.Model):
    ID = models.PositiveBigIntegerField(max_length=20)
    Name = models.CharField(max_length=255)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()